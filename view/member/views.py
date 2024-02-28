from django.shortcuts import render, redirect
from django.views import View

from member.models import Member
from member.serializers import MemberSerializer


# 회원가입
class MemberJoinView(View):
    # 회원가입 페이지로 이동
    # get 메소드를 사용하여 회원가입 페이지 요청:
    def get(self, request):
        # member/join.html 템플릿으로 이동
        return render(request, 'member/join.html')

    # 회원가입 정보 입력 후 로그인 페이지로 이동
    # post 메소드를 사용하여 회원가입 정보 요청:
    def post(self, request):
        # data = post 메소드로 입력 받은 회원가입 정보 가져오기
        data = request.POST
        # 회원가입 정보 모델 속 필드에 입력
        # member-email ... → html input 태그의 name
        data = {
            'member_email': data['member-email'],
            'member_password': data['member-password'],
            'member_name': data['member-name']
        }

        # CRUD 중 C (create)
        # Member 모델 속에 객체 생성 및 테이블에 데이터 추가
        Member.objects.create(**data)

        # 회원가입 완료 후 redirect를 통해 페이지 이동 요청
        # urls: member/login 요청 → loginview: get() 메소드를 사용하여 rander로 경로 받고 login 페이지 이동
        return redirect('member:login')


# 회원 로그인
class MemberLoginView(View):
    # get 메소드를 사용하여 로그인 페이지 요청:
    def get(self, request):
        # member/login.html 템플릿으로 이동
        return render(request, 'member/login.html')

    # post 메소드를 사용하여 로그인 정보 요청:
    def post(self, request):
        # 입력 받은 로그인 정보는 data에 담기
        data = request.POST
        # 로그인 데이터 정보 모델 속 필드에 입력
        data = {
            'member_email': data['member-email'],
            'member_password': data['member-password']
        }

        # CRUD 중 R (read)
        # member = Member 모델 속 해당 조건을 가지는 객체 가져오기
        # exists()를 사용하기 위해 QuerySet 객체로 조회
        member = Member.objects.filter(**data)

        # url = 이동할 주소 담기 (실패 시 로그인 페이지로 이동)
        url = 'member:login'

        # 만약, member가 True면: ( 로그인 성공 시 메인 페이지로 이동)
        if member.exists():
            # 성공
            # 요청 받은 값으로 섹션을 만들기, 'member' 라는 key 값으로 요청 값을 values로 받기
            # member 객체의 직렬화된 값을 'member'에 담기
            # 섹션은 독자적인 저장소
            request.session['member'] = MemberSerializer(member.first()).data
            # url = 메인 페이지로 이동
            # '/' = root
            url = '/'

        # 일괄처리
        # rdirect를 통해 view로 접근해서 해당하는 url로 이동
        return redirect(url)


# 회원 로그아웃
class MemberLogoutView(View):
    # get 메소드를 사용하여 요청하기
    def get(self, request):
        # 로그아웃 시 session은 비우기
        request.session.clear()

        # redirect를 통해 view로 접근하여 로그인 페이지로 이동
        return redirect('member:login')
