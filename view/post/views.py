import math

from django.db import transaction
from django.db.models import F
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member
from post.models import Post



# 유저 정보는 화면에서 바로 받기 때문에 굳이 추가할 필요가 없다.
# settings에 템플릿 urls 세팅이 정해져 있기 때문에 상대경로로 작성
class PostWriteView(View):
    def get(self, request):
        return render(request, 'post/write.html')

    @transaction.atomic
    def post(self, request):
        data = request.POST

        # 직렬화된 상태라 dict 타입 풀어서 생성자에 전달
        member = Member(**request.session['member'])

        data = {
            'post_title': data['post-title'],
            'post_content': data['post-content'],
            'member': member
        }
        post = Post.objects.create(**data)

        return redirect(post.get_absolute_url())

class PostDetailView(View):
    # id 값은 request에 담기지 않기 때문에 post_id를 따로 매개변수로 받기
    def get(self, request):
        post = Post.objects.get(id=request.GET['id'])

        # 실무에서는 ip주소를 담아서 ip 주소당 조회수 +1 하도록 한다.
        post.post_view_count += 1
        post.save(update_fields=['post_view_count'])

        context = {
            'post': post
        }

        return render(request, 'post/detail.html', context)


class PostUpdateView(View):
    # 1. get 수정 페이지 이동
    # - post id 가져오기
    # - 포스트 정보 가져오기
    # 포스트 내용 받아서 innerTEXT로 화면에 뿌려줘야 하지 않을까?
    def get(self, request):
        post = Post.objects.get(id=request.GET['id'])
        return render(request, "post/update.html", {'post': post})

    # 2. post 수정정보 입력 > 완료
    # - 포스트 수정 정보 입력 완료
    # - update 쿼리 날리기
    # 3. 디테일 페이지로 이동
    def post(self, request):
        data = request.POST

        post_id = data['id']
        post = Post.objects.get(id=post_id)

        post.post_title = data['post-title']
        post.post_content = data['post-content']
        post.save(update_fields=['post_title', 'post_content'])

        return redirect(post.get_absolute_url())


class PostDeleteView(View):
    def get(self, request):
        # update 쿼리
        Post.objects.filter(id=request.GET['id']).update(post_status=False)

        # save 쿼리
        # post = Post.objects.get(id=request.GET['id'])
        # post.status =False
        # post.save(update_fields=['status'])

        return redirect('/post/list')


class PostListView(View):
    def get(self, request):
        return render(request, 'post/list.html')


# APIView 상속을 받는 순간 REST가 된다.
class PostListAPI(APIView):
    # page는 전달받은 게 없으면 1을 가져오도록 html에서 설정되어 있음!
    def get(self, request, page):
        # 페이지 이동이된 상태에서 이동하기 때문에 None이 없음
        # 행 개수.(한 페이지에 보여질 게시물 개수
        row_count = 5

        # 0:5 > 마지막은 미포함
        offset = (page - 1) * row_count
        limit = page * row_count

        # 쿼리셋 객체로 들어가면 안됨! values를 사용하여 dict 형식으로 가져오기
        columns = [
            'id',
            'post_title',
            'post_content',
            'post_view_count',
            'member_name'
        ]

        # list언패킹은 별 한개
        posts = Post.enabled_objects \
                    .annotate(member_name=F('member__member_name')) \
                    .values(*columns)[offset:limit]

        has_next = Post.enabled_objects.filter()[limit:limit + 1].exists()

        post_info = {
            'posts': posts,
            'hasNext': has_next
        }

        # 자동으로 json 형태로 가져오기 때문에 직렬화가 필요 없다.
        # response라는 객체에서 전달이 되는 것!
        return Response(post_info)
