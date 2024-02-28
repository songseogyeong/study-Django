from django.db.models import Count, F
from django.test import TestCase

from member.models import Member
from post.models import Post
from reply.models import Reply
from random import randint

class ReplyTests(TestCase):
    # 실습 1번. (팀 진행)
    # 나이가 30 이상인 회원이 작성한 댓글의 게시물 제목 및 회원의 이름 조회

    # 실습 1번 1.
    # 모든 게시글에 댓글 10개씩 추가
    # 댓글은 랜덤한 회원을 작성자로 설정하기

    # list 초깃값을 가지는 replies 변수 선언
    replies = []

    # 멤버, 게시글 가져오기
    # members_queryset = Member 모델 속 객체를 모두 가져오기
    members_queryset = Member.objects.all()
    # posts_queryset = Post 모델 속 객체를 모두 가져오기
    posts_queryset = Post.objects.all()

    # 10번 반복하여 i에 하나씩 담아주기
    for i in range(10):
        # posts_queryset 객체를 반복하여 post에 하나씩 담기
        for post in posts_queryset:
            # reply 데이터 입력
            reply = {
                'reply_content': f'테스트댓글{i + 1}',
                'member': members_queryset[randint(0, len(members_queryset) - 1)],
                'post': post,
                'reply_private_status': randint(0,1)
            }
            # replies에 reply 객체 추가
            # reply는 dict 타입이기 때문에 Reply 모델로 감싸서 추가하기
            replies.append(Reply(**reply))


    # 실습 1번 2.
    # 게시글 안에 댓글 만들기
    # Reply 모델 속 replies 객체 생성 후 테이블에 데이터 저장
    Reply.objects.bulk_create(replies)


    # 실습 1번 3.
    # 나이가 30 이상인 회원이 작성한 댓글의 게시물 제목 및 회원의 이름 조회
    # Reply 모델 속 member의 나이가 30 이상인 객체의 post_title, member_name 필드 값만 가져와 reply_list에 담기
    reply_list = Reply.objects.filter(member__member_age__gte=30).values('post__post_title', 'member__member_name')
    for reply in reply_list:
        print(reply)


    # 실습 2번.
    # 댓글을 작성한 회원들중에서 댓글을 2개 이상 작성한 유저 찾기 (회원이름만 찾기)

    # Reply 모델 속 member 필드의 id 개수를 세고 개수 값은 id_count 별칭을 설정하여 담아주기
    # id_count가 2개 이상이면, member_name 값을 가져오고 reply_list 변수에 담기
    reply_list = Reply.objects.values('member').annotate(id_count=Count('id')).filter(id_count__gte=2).values('member__member_name')
    # reply_list 반복하여 reply 하나씩 담기:
    for reply in reply_list:
        # reply 출력
        print(reply)


    # 실습 3번.
    # 게시글과 댓글을 모두 작성한 회원을 찾으세요

    # 실습 3번 1. 로그인
    # 로그인 데이터 입력
    member_data = {
        'member_email': 'test4@gmail.com',
        'member_password': '1234'
    }

    # 로그인 검사, 로그인 정보
    # member = Member 모델의 data 값을 가지는 객체를 조회하여 가져오기
    member = Member.enabled_objects.get(**member_data)


    # 실습 3번 2. 게시물 선택
    # post = Post 모델 속 id 필드의 값이 7인 객체 가져오기
    post = Post.objects.get(id=7)


    # 실습 3번 3. 댓글 추가
    # reply_data 데이터 입력
    reply_data = {
        'reply_content': '댓글 테스트1',
        'member': member,
        'post': post
    }

    # reply_data 데이터를 받아 Reply 모델 속 객체 생성하는 쿼리 reply 담기
    reply = Reply.objects.create(**reply_data)
    # reply 객체 생성 시 group_id 필드의 값은 id 필드의 값과 동일
    reply.group_id = reply.id
    # reply 객체 추가
    # save 추가 또는 수정
    reply.save()


    # 실습 4번.
    # 대댓글 3개 등록하기
    # 실행 3번으로 3개 등록하기

    # 실습 4번 1.
    # 로그인 데이터 입력
    member_data = {
        'member_email': 'test4@gmail.com',
        'member_password': '1234'
    }

    # 로그인 검사
    # member = Member 모델의 data 값을 가지는 객체를 조회하여 가져오기
    member = Member.objects.get(**member_data)


    # 실습 3번 2. 게시물 선택
    # post = Post 모델 속 id 필드의 값이 7인 객체 가져오기
    post = Post.objects.get(id=7)


    # 실습 3번 3. 댓글 선택
    # Reply 모델 속 post_id 필드의 값이 7이고 reply_depth 필드 값이 1인 조건을 가지는 객체를 가져오기
    # 가져온 객체의 0번째 값 가져와 reply 변수에 담기
    # 어차피 가져오는 값은 1개이긴 하지만, 인덱스 번호를 선택해 특정 값을 가져오기
    reply = Reply.objects.filter(post_id=post.id, reply_depth=1)[0]


    # 실습 3번 4. 대댓글 입력
    # re_reply_data 데이터 입력
    # member: 로그인된 회원의 데이터 받기
    # post: 선택된 게시글 데이터 받기
    # group_id: 선택된 댓글 데이터의 id 받기
    # reply_depth: 대댓글이기 때문에 댓글 +1 깊이 정해주기
    re_reply_data = {
        'reply_content': '대댓글 테스트1',
        'member': member,
        'post': post,
        'group_id': reply.id,
        'reply_depth': reply.reply_depth + 1
    }


    # 실습 3번 5. 대댓글 추가
    # re_reply_data 데이터 받아 Reply 속 객체 생성 후 테이블에 데이터 추가해주는 쿼리를 re_reply 담기
    re_reply = Reply.objects.create(**re_reply_data)
    # 대댓글 추가
    re_reply.save()

    # replies = Reply 모델 속 group_id가 2 조건을 가지는 객체 가져오기
    replies = Reply.objects.filter(group_id=2)
    # replies 반복하여 reply 하나씩 담기
    for reply in replies:
        # reply의 reply_private_status을 출력하기
        # get_선택 이름_display()
        # _display() 메소드를 통해 상태를 텍스트로 표기
        # 출력 결과: 일반 댓글 (status = 0 = False)
        print(reply.get_reply_private_status_display())


    # 실습 4번.
    # 게시글 상세보기
    # 게시글 정보, 회원정보, 댓글 목록, 댓글의 대댓글 목록

    # 실습 4번 1. 게시글 정보 가져오기
    # 7번 게시글의 내용과 작성자 정보를 가져온다
    # Post 모델 속 id가 7번 조건인 객체를 가져오기
    # member__member_name 필드 별칭은 member_name 설정
    # 가져온 객체 중 첫번째 객체의 아래 값들을 가져와 post에 담기
    post = Post.objects.filter(id=7) \
        .annotate(member_name=F('member__member_name')) \
        .values('id', 'post_title', 'post_content', 'member__member_name').first()


    # 실습 4번 2. 댓글 목록 가져오기
    # Reply 모델 속 post_id가 post의 id 필드 값과 같고 reply_depth가 1 조건을 가지는 객체를 가져와 replies 담기
    replies = Reply.objects.filter(post_id=post['id'], reply_depth=1)

    # replies 반복해 reply 하나씩 담기:
    for reply in replies:
        # reply 출력
        print(reply)


    # 실습 4번 3. 대댓글 목록 가져오기
    # 댓글 데이터 입력
    data = {
        'id': 2
    }

    # 전달받은 댓글의 대댓글을 모두 가져온다
    # Reply 모델 속 group_id 값이 data의 id와 같고 reply_depth가 2 조건을 가지는 객체를 가져와 re_replies 담기
    re_replies = Reply.objects.filter(group_id=data['id'], reply_depth=2)


    # 실습 4번 4. 게시글을 작성한 적이 있는 회원 목록 출력
    # members = Member 모델 속 post가 null이 아닌 조건을 가지는 객체의 모든 필드의 값을 가져오기
    members = Member.objects.filter(post__isnull=False).values()
    # members 반복하여 member 담기:
    for member in members:
        # member 출력
        print(member)

    # 실습 4번 5. 대댓글을 작성한 적이 없는 회원 목록 출력
    # members = Member 모델 속 reply__reply_depth=2 조건을 가지지 않는 객체의 id, reply 필드 값 가져오기
    # exclude 메소드는 지정된 조건을 만족하지 않는 객체만 가져온다.
    members = Member.objects.exclude(reply__reply_depth=2).values('id', 'reply')
    # members 반복하여 member 하나씩 담기:
    for member in members:
        # member 출력
        print(member)


    # + 사용할 일 x
    # 실습 4번 4. 게시글을 작성한 적이 있는 회원 목록 출력
    # replies = Reply 모델 속 reply_depth=2 조건을 가지는 객체의 member_id 필드 값 가져오기
    replies = Reply.objects.filter(reply_depth=2).values('member_id')
    # set() 메소드를 member_ids 변수에 담기 (중복 허용 X)
    # tuple 타입
    member_ids = set()
    # replies 반복하여 reply 하나씩 담기:
    for reply in replies:
        # reply의 member_id 값을 가지는 객체를 member_ids에 추가
        member_ids.add(reply['member_id'])


    # 실습 4번 5. 대댓글을 작성한 적이 없는 회원 목록 출력
    # members= Member 모델 속 id 필드에 member_ids가 있지 않는 객체의 값을 가져오기
    members = Member.objects.exclude(id__in=member_ids).values()
    # members 반복하여 member 하나씩 담기:
    for member in members:
        # member 출력
        print(member)
