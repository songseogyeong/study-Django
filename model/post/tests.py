from django.db.models import Q, Count
from django.test import TestCase
from member.models import Member
from post.models import Post
from random import randint


class PostTest(TestCase):
    # 실습 1번
    # 총 98개의 게시글 작성
    # 랜덤한 회원을 작성자로 설정

    # list 값을 가지는 초깃값 설정
    posts = []

    # Member 모델에서 모든 필드를 가져오고 members_queryset 변수에 담기
    members_queryset = Member.objects.all()

    # 98번 반복하여 i에 담기:
    for i in range(98):
        # dict 타입의 값 선언
        # member: 0부터 member_queryest 길이 - 1까지 랜덤한 숫자를 members_queryset[인덱스 번호] 값으로 설정
        # 인덱스 번호가 0부터 시작하기 때문에 -1 해주기
        post = {
            'post_title': f'테스트 제목{i + 1}',
            'post_content': f'테스트 내용{i + 1}',
            'member': members_queryset[randint(0, len(members_queryset) - 1)]
        }
        # posts에 post 값들을 추가해주기
        # **post는 dict 객체이기 때문에 객체로 만들기
        posts.append(Post(**post))

    # Post 모델 속 필드에 posts 값 추가
    # 여러개의 객체를 추가하기 때문에 bulk_create 사용
    Post.objects.bulk_create(posts)


    # 실습 2번
    # 로그인된 회원의 마이페이지에서 내가 작성한 게시글 조회하기
    # 아이디가 3이고 일반 회원 정보를 조회

    # Member 모델에서 member_status가 일반 회원(True)이고, id가 3인 회원 객체를 가져오기
    # 값은 member 변수에 담기
    member = Member.objects.get(member_status=True, id=3)
    # member의 값을 dict 형식으로 출력
    print(member.__dict__)

    # _set을 이용해 역참조하여 해당하는 member의 모든 post를 가져오기
    # 가져온 값은 반복하여 post에 하나씩 담기:
    for post in member.post_set.all():
        # post 출력
        print(post)


    # 실습 3번
    # 나이가 30 미만인 회원이 작성한 게시글 목록 조회
    # 단, 회원의 이름과 나이까지 같이 조회하기

    # 1. 정방향으로 직접 참조
    # Post 모델에서 member 필드 속 member_age가 30 미만인 값을 가져오기
    # 가져온 값은 post_list에 담기
    post_list = Post.objects.filter(member__member_age__lt=30)

    # post_list 반복하여 post에 값을 하나씩 담기:
    for post in post_list:
        # 원하는 key 값 출력
        # post.id = post.pk
        print(post.id, post.post_title, post.post_content, post.member.member_name, post.member.member_age)

    # 2. 한번에 참조(member__member_name, member__member_age)
    # Post 모델에서 member 필드 속 member_age가 30 미만인 값을 가져오기
    # 가져오고자 하는 값은 values로 설정하고 post_list에 담기
    post_list = Post.objects.filter(member__member_age__lt=30).values('id', 'post_title', 'post_content', 'member__member_name', 'member__member_age')

    # post_list 반복하여 post에 값을 하나씩 담기:
    for post in post_list:
        # post 출력
        print(post)


    # 실습 4번
    # 회원의 나이가 20이상 30이하인 회원이 작성한 게시글 중 post_title에 "테"가 들어가고 내용에 "7"로 끝나는 게시글 정보 조회
    # Member는 사용하지 않고 Post만 사용해서 하기
    # 나이 범위는 __range를 사용해서 진행

    # 조건 설정
    conditions1 = Q(member__member_age__range=(20, 30))
    conditions2 = Q(post_title__contains='테')
    conditions3 = Q(post_content__endswith='7')
    conditions = conditions1 & conditions2 & conditions3

    # Post 모델에서 conditions 조건에 해당하는 values 가져오기
    # 값은 post_list에 담기
    post_list = Post.objects.filter(conditions).values('post_title', 'post_content')
    # post_list는 반복하여 post에 담기:
    for post in post_list:
        # post 출력
        print(post)


    # 실습 5번
    # 게시물을 2개 이상 작성한 회원의 id와 이름을 조회
    # id를 오래된순으로 정렬

    # Post 모델 속 member 필드의 id 개수 연산 후 별칭 id_count로 설정
    # in_count가 2개 이상(gte)인 값의, values 가져오기
    # 값은 post_list 담기
    post_list = Post.objects.values('member').annotate(id_count=Count('id')).filter(id_count__gte=2).values('member__id', 'member__member_name').order_by('member_id')
    # post_list 반복하여 post에 하나씩 담기:
    for post in post_list:
        # post 출력
        print(post)


    # 실습 6번
    # 게시글을 작성한 회원 중에서 게시글을 15개 이상 작성한 회원 찾기

    # Post 모델 속 해당하는 필드의 values를 가져오는데,
    # member_id 개수를 카운트하여 member_count 별칭으로 설정하고
    # member_count가 15개 이상인 값만 가져오기
    # 값은 posts에 담기
    posts = Post.objects.values(
        'member_id',
        'member__member_name',
        'member__member_age',
        'member__member_email') \
        .annotate(member_count=Count('member_id')) \
        .filter(member_count__gte=15)

    # posts는 반복하여 post에 하나씩 담기
    for post in posts:
        # post 출력
        print(post)


    # 내·외부 조인
    # A필드에 b가 있다고 가정
    # a.b (정참조): a로 b필드에 접근하면 정방향 참조이고, b의 null 상태에 따라 내부 또는 외부조인이 실행된다.
    # * null 허용 시 외부조인, null 비허용 시 모두 True가 되기 때문에 내부조인
    # b.a (역참조): b로 a필드에 접근하면 역방향 참조이고, b의 모든 정보가 나와야하기 때문에 항상 외부조인이 실행된다.

    # EAGER(즉시)
    # 실행하는 순간 쿼리가 실행된 뒤, 이후 쿼리가 발생하지 않는다.
    # 하나의 서비스에서 여러 번 JOIN해야 할 경우 사용한다.
    # * 쿼리를 한번 날리고 값을 가져온다(성능 향상).
    # * 쿼리 출력 시 모든 값을 가져오기 때문에 JOIN이 많을 때는 사용을 지양
    posts = Post.objects.select_related('member', 'reply', 'category').values('id', 'post_title', 'member__member_name')
    for post in posts:
        print(post)
    # * select_related를 사용하여 쿼리를 한번에 날리고 값을 가져올 수 있다.

    # LAZY(지연)
    # 실행할 때 쿼리가 만들어지고 필드에 접근할 때마다 쿼리가 발생한다.
    # * 객체에 접근할 때마다 쿼리 날리기
    # all()[:} all() 후 slicing 시 lazy 사용
    print(Post.objects.values('member__member_name').query)
    # 출력 결과: INNER JOIN
    # * post에서 member 값을 가져오기 때문에 정참조가 되며, 내부조인이 된다.
    print(Member.objects.values('post__post_title').query)
    # 출력 결과: LEFT OUTER JOIN
    # * Member에서 post 값을 가져오기 때문에 역참조가 되며, 외부조인이 된다.
