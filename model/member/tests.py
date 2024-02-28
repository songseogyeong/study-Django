from django.test import TestCase
from django.db.models import Q, Count, Max, Min, F

from member.models import Member
from post.models import Post
from reply.models import Reply


class MemberTest(TestCase):
    # 클래스 내부에 코드를 작성하면 연결한 테이블에 저장되고,
    # 메소드 내에서 코드를 작성하면 임시 테이블에 저장된 뒤 사라진다.
    # (예시) def ...

    # 1번. create
    # member = Member 모델 속 객체 생성
    member = Member.objects.create(
        member_email='test1@gmail.com',
        member_password='1234',
        member_age=20,
        member_name='테스트1',
    )

    # member를 dict 형식으로 출력
    print(member.__dict__)

    # 메소드 내 코드 작성(테이블 저장X)
    def test_member_creation(self):
        # member = Member 모델 속 객체 생성
        member = Member.objects.create(
            member_email='test1@gmail.com',
            member_password='1234',
            member_age=20,
            member_name='테스트1',
        )
        # member를 dict 형식으로 출력
        print(member.__dict__)


    # 실습 1번. create
    # 실습 1번 1. 회원 1명 추가
    # Member 모델 속 객체 생성
    Member.objects.create()

    # 실습 1번 2. 회원 2명 추가
    # 2번 반복하여 i 속에 하나씩 담기:
    for i in range(2):
        # Member 모델 속 객체 생성
        Member.objects.create()


    # 2번. save
    # member 데이터 입력
    datas = {
        'member_email': 'test2@gmail.com',
        'member_password': '1234',
        'member_age': 20,
        'member_name': '테스트2',
    }
    # member = Member 모델에 datas 전달
    member = Member(**datas)
    # member 추가하기
    member.save()


    # 실습 2번 1. 회원 1명 추가
    # dict 초깃값을 가지는 datas 변수 선언
    datas = {}

    # member = Member 모델에 datas 전달
    member = Member(**datas)
    # member 추가하기
    member.save()

    # 실습 2번 2. 회원 2명 추가
    # list 안에 dict 초깃값을 가지는 datas 변수 선언
    datas = [
        {},
        {},
    ]

    # datas 반복하여 data 속에 하나씩 담기:
    for data in datas:
        # member = Member 모델에 datas 전달
        member = Member(**data)
        # member 추가하기
        member.save()


    # 3번. bulk_create
    # members = Member 모델 속 다수의 객체 생성
    # 다수의 객체 생성 시 bulk_create 사용하며, id는 자동 생성이기 때문에 입력하지 않는다.
    members = Member.objects.bulk_create([
        Member(
            member_email='test3@gmail.com',
            member_password='1234',
            member_age=10,
            member_name='테스트3'),
        Member(
            member_email='test4@gmail.com',
            member_password='1234',
            member_age=30,
            member_name='테스트4'),
        Member(
            member_email='test5@gmail.com',
            member_password='1234',
            member_age=40,
            member_name='테스트5')
    ])

    # members 반복하여 member 속에 하나씩 담기:
    for member in members:
        # member는 dict 형식으로 출력
        print(member.__dict__)


    # 3번 1. 회원 2명 추가
    # list 안에 dict 초깃값을 가지는 datas 변수 선언
    datas = [
        {},
        {}
    ]

    # list 초깃값을 가지는 member 변수 선언
    members = []

    # datas 반복하여 data 속에 하나씩 담기:
    for data in datas:
        # members에 data 객체 추가
        # 다수의 값이기 때문에 Member 모델로 감싸서 추가
        members.append(Member(**data))

    # Member 모델 속 객체 생성 후 테이블에 저장
    Member.objects.bulk_create(members)


    # 4번. get_or_create
    # member 데이터 입력
    datas = {
        'member_password': '1234',
        'member_age': 50,
        'member_name': '테스트6',
    }

    # test6@gmail.com 회원 정보 조회 후 회원이 없으면 새로운 정보를 전달하여 회원 추가
    # Member 모델 속 객체 생성
    # member에 회원 정보 조회, created에 회원 정보가 없을 시 추가할 정보를 받기
    member, created = Member.objects.get_or_create(member_email='test6@gmail.com', defaults=datas)
    # member는 dict 형식, created 함께 출력
    print(member.__dict__, created)


    # 실습 4번 1.
    # member_email이 'admin1@gmail.com'인 회원을 조회한다.
    # 만약 없으면 새로운 정보를 전달하여 회원을 추가한다.

    # dict 초깃값을 가지는 datas 변수 선언
    datas = {}

    # Member 모델 속 객체 생성
    # member에 회원 정보 조회, created에 회원 정보가 없을 시 추가할 정보를 받기
    member, isCreated = Member.objects.get_or_create(member_email='admin1@gmail.com', defaults=datas)


    # 5번. get
    # member = Member 모델 속 id가 3인 객체를 가져오기 (단일 객체)
    member = Member.objects.get(id=3)
    # member dict 형식으로 출력
    print(member.__dict__)


    # 6번. all
    # members = Member 모델 속 모든 객체를 가져오기
    members = Member.objects.all()
    # members = Member 모델 속 True 값인 모든 객체를 가져오기
    # enabled_objects 매니저 사용으로 True 값만 반환
    members = Member.enabled_objects.all()
    # members 반복하여 member 속에 하나씩 담기:
    for member in members:
        # member dict 형식으로 출력
        print(member.__dict__)

    # 7번. filter
    # member_queryset = Member 모델 속 member_name='테스트6' 조건을 가지는 True 값인 객체 가져오기
    member_queryset = Member.enabled_objects.filter(member_name='테스트6')
    # member_querysetf의 값 출력
    # exists() 메소드 사용으로 True 또는 False 값만 반환
    print(member_queryset.exists())
    # member_querysetf의 0번째 인덱스 번호의 값을 dict 형식으로 출력
    print(member_queryset[0].__dict__)

    # 8번. contains
    # member_queryset = Member 모델 속 member_name 필드 값에 '테'를 포함하는 조건을 가지는 True 값인 객체 가져오기
    member_queryset = Member.enabled_objects.filter(member_name__contains='테')
    # member_querysetf의 값 출력
    # exists() 메소드 사용으로 True 또는 False 값만 반환
    print(member_queryset.exists())
    # member_queryset 반복하여 member 속에 하나씩 담기:
    for member in member_queryset:
        # member는 dict 형식으로 출력
        print(member.__dict__)


    # 9번. startswith, endswith
    # member_queryset = Member 모델 속 member_name 필드 값에 '테'로 시작하는 조건을 가지는 True 값인 객체 가져오기
    member_queryset = Member.enabled_objects.filter(member_name__startswith='테')
    # member_querysetf의 값 출력
    # exists() 메소드 사용으로 True 또는 False 값만 반환
    print(member_queryset.exists())
    # member_queryset 반복하여 member 속에 하나씩 담기:
    for member in member_queryset:
        # member는 dict 형식으로 출력
        print(member.__dict__)

    # member_queryset = Member 모델 속 member_name 필드 값에 '3'으로 끝나는 조건을 가지는 True 값인 객체 가져오기
    member_queryset = Member.enabled_objects.filter(member_name__endswith='3')
    # member_querysetf의 값 출력
    # exists() 메소드 사용으로 True 또는 False 값만 반환
    print(member_queryset.exists())
    # member_queryset 반복하여 member 속에 하나씩 담기:
    for member in member_queryset:
        # member는 dict 형식으로 출력
        print(member.__dict__)


    # 10번. in
    # member_queryset = Member 모델 속 True인 객체를 가져오는데,
    # member_email이 'test3@gmail.com', 'test6@gmail.com' 조건 값을 가지는 객체의 member_email 필드 값만 가져오기
    member_queryset = Member.enabled_objects.filter(member_email__in=['test3@gmail.com', 'test6@gmail.com']).values('member_email')
    # member_queryset의 쿼리를 출력
    # 어떤 베이스의 어떤 쿼리가 실행되는지 알 수 있다.
    print(member_queryset.query)
    # member_queryset 반복하여 member 속에 하나씩 담기:
    for member in member_queryset:
        # member의 member_email 필드 값만 출력
        print(member.get('member_email'))


    # 11번. exclude()
    # member_queryset = Member 모델 속 True인 객체를 가져오는데,
    # member_email='test3@gmail.com'를 만족하지 않는 객체의 member_email 필드 값을 가져오기
    member_queryset = Member.enabled_objects.exclude(member_email='test3@gmail.com').values('member_email')

    # member_queryset 반복하여 member 속에 하나씩 담기:
    for member in member_queryset:
        # member의 member_email 필드 값 출력
        print(member["member_email"])


    # 12번. AND, OR
    # member_queryset = Member 모델 속 status가 True 조건을 가지고, member_age가 30 초과인 객체 가져오기
    member_queryset = Member.objects.filter(status=True) & Member.objects.filter(member_age__gt=30)

    # condition1 = status=True (=정상 회원) 조건
    condition1 = Q(status=True)
    # condition2 = member_age = 30 초과 조건
    condition2 = Q(member_age__gt=30)
    # member_queryset = Member 모델 속 condition1과 condition2 조건을 가지는 객체 가져오기
    member_queryset = Member.objects.filter(condition1 & condition2)
    # member_queryset = Member 모델 속 condition1 또는 condition2 조건을 가지는 객체 가져오기
    member_queryset = Member.objects.filter(condition1 | condition2)

    # member_queryset 반복하여 member 속에 하나씩 담기:
    for member in member_queryset:
        #  member_email와 member_age 사이에 , 값을 넣어 출력하기
        print(member.member_email, member.member_age, sep=", ")


    # 13번. order_by
    # member_queryset = Member 모델 속 모든 객체를 가져오는데, 내림차순 정렬하기
    member_queryset = Member.objects.all().order_by('-id')
    # member_queryset 반복하여 member 속에 하나씩 담기:
    for member in member_queryset:
        # member는 dict 형식으로 출력하기
        print(member.__dict__)


    # 14번. aggregate
    # annotate()는 QuerySet객체로 리턴하기 때문에 뒤에 이어서 추가 작업이 가능하지만,
    # aggregate()는 전체 대상이므로 뒤에 이어서 추가 작업이 불가능하다.

    # member = Member 모델 속 member_age 필드의 최댓값과 최솟값을 가져오기
    member = Member.objects.aggregate(max_age=Max('member_age'), min_age=Min('member_age'))
    # 최댓값, 최솟값 출력
    print(member['max_age'], member['min_age'])



    # 15번. range
    # filter(필드명__range=[이상, 이하])
    # range는 사이값을 구해준다.


    # 실습 15번. range
    # 회원의 나이가 20이상 30이하인 회원이 작성한 게시글 중 post_title에 "테"가 들어가고 내용에 "7"로 끝나는 게시글 정보 조회
    # Member는 사용하지 않고 Post만 사용해서 하기
    # 나이 범위는 __range를 사용해서 진행

    # 실습 15번 1. 역참조
    # members = Member 모델 속 조건에 맞는 객체의 값을 가져오기
    # 모든 값을 가지고 올 때는 values() 값을 비워 가져올 수 있다.
    members = Member.objects.filter(member_age__range=[20, 30], post__post_title__contains='테', post__post_content__endwith='7').values()

    # members 반복하여 member 속에 담기:
    for member in members:
        # member 출력
        print(member)


    # 실습 15번 2. 정참조
    # posts = Post 모델 속 조건에 해당하는 객체를 가져오기
    posts = Post.objects.filter(member__member_age__range=[20, 30], post_title__contains='테', post_content__endwith='7')
    # posts 반복하여 post 속에 하나씩 담기:
    for post in posts:
        # post 출력
        print(post)


    # 실습 16번. 로그인된 회원의 상세페이지에서 내가 등록한 맵주소 찾기
    # 실습 16번 1. 로그인
    # 로그인 데이터 입력
    data = {
        'member_email': 'test4@gmail.com',
        'member_password': '1234'
    }

    # member = Member 모델의 data 값을 가지는 객체를 조회하여 가져오기
    member = Member.enabled_objects.get(**data)


    # 실습 16번 2. 맵주소 찾기
    # member_address 필드 값 출력
    # print(member.member_address)


    # 실습 16번 3. 이름 찾기
    # member_name 필드 값 출력
    print(member.member_name)


    # 실습 17번. 게시글과 댓글을 모두 작성한 회원을 찾으세요
    # 화면 예시: 회원 정보, 게시글 개수, 댓글 개수

    # DBMS 쿼리 입력
    query = """
        select
        select * m.id, m.member_email, m.member_name, count(p.id)
        from tbl_member m left outer join tbl_post p
        on m.id = p.memeber_id
    """

    # Member 모델 속 해당하는 필드의 개수를 구하고 별칭 두기
    Member.objects.values('id', 'member_email', 'member_name', 'reply__id') \
        .annotate(post_count=Count('post'), reply_count=Count('reply__id')) \
        .annotate(post_count=Count('post'))

    # member = reply_id 필드의 reply_count의 개수를 구하고 별칭 두기
    members = members.values('reply_id').annotate(reply_count=Count(''))

    # members 반복하여 member 속에 하나씩 담기:
    for member in members:
        # member 출력
        print(member)



    # 실습 18번. 회원 이름이 "테스트6"이거나 회원 나이가 30 이상인 회원이 작성한 게시글 목록 조회
    # name_condition = member_name이 '테스트6'인 조건
    name_condition = Q(member_name='테스트6')
    # age_condition = member_age가 30 이상인 조건
    age_condition = Q(member_age__gte=30)
    # condition = name_condition 또는 age_condition
    condition = name_condition | age_condition

    # members = Member 모델 속 조건에 맞는 객체의 모든 값을 가져오기
    members = Member.objects.filter(condition).values()

    # members 반복하여 member 속에 하나씩 담기:
    for member in members:
        # member 출력
        print(member)


    # 19번. serch
    # OR: |=
    # 조건식의 초깃값
    condition = Q()

    # 필터 검색 활용 가능
    # 둘 중 하나가 참이면 모두 참
    condition |= name_condition
    condition |= age_condition


    # AND: &=
    # 다중선택
    # 데이터 입력
    data = {
        'region': '',
        'color': 'red',
        'date': '2019-05-01'
    }

    # 조건 담기
    region_condition = Q(region=data['region'])
    color_condition = Q(region=data['color'])

    # 조건식의 초깃값
    condition = Q()

    # 둘 다 참이여야 참
    if data.region:
        condition &= region_condition

    if data.color:
        condition &= color_condition

    # posts = Post 모델 속 조건을 해당하는 객체 가져오기
    posts = Post.objects.filter(condition)
    # posts 반복하여 post 속에 하나씩 담기:
    for post in posts:
        # post 출력
        print(post)


    # 20번. save
    # 실습 20번. 회원 이름 수정
    # 로그인 데이터 입력
    data = {
        'member_email': 'test1@gmail.com',
        'member_password': '1234'
    }

    # member = Member 모델의 data 값을 가지는 객체를 조회하여 가져오기
    member = Member.objects.get(**data)

    # 모든 객체의 필드 값 변경
    # 변경할 데이터 담기
    member.member_name = '수정된 이름'
    member.member_password = '3333'
    # save()로 필드의 모든 값 변경
    member.save()

    # 각 객체의 필드 값 변경
    # 변경할 데이터 담기
    member.member_name = '수정된 이름'

    # save()시 모든 필드가 변경이 되기 때문에, update_fields로 어떤 필드를 변경할 건지 알려주기
    member.save(update_fields=['member_name'])


    # 21번. update
    # 실습 21번 1. 회원의 이름 변경
    # 로그인 데이터 입력
    data = {
        'member_email': 'test1@gmail.com',
        'member_password': '1234'
    }

    # member = Member 모델의 data 값을 가지는 객체를 조회하여 가져오기
    member = Member.objects.filter(**data)

    # count= member 객체의 member_name 필드 값 변경
    count = member.update(member_name='다시 수정된 이름')
    # count 출력
    print(count)

    # count = Member 모델 속 모든 객체의 member_name 변경
    # filter가 없기 때문에 모든 값을 수정한다.
    count = Member.objects.update(member_name='수정된 이름')
    # count 출력
    print(count)


    # 실습 21번 2. 나이가 20살 이하인 회원의 나이를 +1한다.
    # count = Member 모델 속 member_age가 20이하인 조건을 가지는 객체를 가져오고,
    # member_age 필드를 member_age + 1 로 변경한다.
    count = Member.objects.filter(member_age__lte=20).update(member_age=F('member_age') + 1)
    # count 출력
    print(count)


    # 22번. delete
    # try 문에 담아 오류 시 except가 실행되게 하기
    try:
        # coutn = Member 모델 속 id가 26인 객체를 삭제
        count = Member.objects.get(id=26).delete()
        # count 출력
        print(count)

    # 위 쿼리가 ProtectedError 오류라면:
    except ProtectedError:
        # 'ProtectedError' 문자열 출력하기
        print('ProtectedError')
