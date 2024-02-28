from django.db.models import Q
from django.test import TestCase

from friend.models import Friend
from member.models import Member


class FriendTest(TestCase):
    # 1번. 회원가입
    # 회원가입 될 회원 정보 data에 받기
    data = {
        'member_email': 'hoon@naver.com',
        'member_password': 'zzzz',
        'member_name': '훈이',
        'member_age': 5
    }

    # data 값을 받아 객체 생성 후 테이블에 저장
    Member.objects.create(**data)


    # 2번. 로그인
    # 로그인 정보 data에 받기
    data = {
        'member_email': 'zzanggu@naver.com',
        'member_password': 'zzzz'
    }

    # 보내는 사람 = Member 모델의 data 값을 가지는 객체 가져오기
    sender = Member.objects.get(**data)


    # 3번. 친구 요청
    # 받는 사람 정보 data에 받기
    data = {
        'member_email': 'yuri@naver.com',
    }

    # 받는 사람 = data의 member_email 값을 가지는 객체를 가져오고 member_email로 별칭 설정
    receiver = Member.objects.get(member_email=data['member_email'])

    # Friend 모델 속 sender 필드 값은 sender으로, receiver 필드 값은 receiver로 설정하여 객체 생성 후 테이블에 저장
    Friend.objects.create(sender=sender, receiver=receiver)


    # 4번. 친구 요청 조건 (False 때만 요청 가능)
    # 중복해서 친구 요청이 가지 않도록 제어하는 조건식

    # Friend 모델 속 receiver 필드에 값 유무에 따라 exists로 True 혹은 False 값이 나오게 하기
    # 값은 condition 변수에 담기
    condition = Friend.objects.filter(receiver=receiver).exists()
    # condition 출력
    print(condition)

    # receiver, sender 값 검사 조건을 condition_exist 변수에 담기
    condition_exist = Q(receiver=receiver, sender=sender)
    # status = 1 (승인) 혹은 status = 0 (대기) 값 검사 조건을 condition_status 변수에 담기
    condition_status = Q(status=1) | Q(status=0)
    # condition_exist 그리고 conditions_status 둘 다 해당하는지에 대한 값 검사 조건을 condition 변수에 담기
    condition = condition_exist & condition_status

    # Friend 모델 필드 값이 condition에 해당하는지 검사 후 검사 결과에 따라 exists로 True 혹은 False 값이 나오게 하기
    # 값은 condition 변수에 담기
    condition = Friend.objects.filter(condition).exists()
    # condition 출력
    print(condition)


    # 5번. 친구 목록
    # 5번 1. 로그인
    # 로그인 데이터 받기
    data = {
        'member_email': 'yuri@naver.com',
        'member_password': 'zzzz'
    }

    # member = Member 모델의 data 값을 가지는 객체 가져오기
    member = Member.objects.get(**data)

    # 5번 2. 친구 요청을 보냈거나 받은 목록에서 친구 수락이 된 정보 모두 조회
    # Fireds 모델 속 firends_objects 매니저에서 filter_member라는 메소드를 가져오기
    # status=True(=1 =승인)인 member 값만 가져와 friends에 담기
    # 로그인된 회원의 승인된 친구목록 가져오기
    friends = Friend.friends_objects.filter_member(member, status=True)
    # friends 반복하여 friend 하나씩 담기
    for friend in friends:
        # 친구 목록 출력
        print(friend.friend)


    # 6번. 친구 삭제 및 거절
    # 로그인 데이터 받기
    data = {
        'member_email': 'yuri@naver.com',
        'member_password': 'zzzz'
    }

    # member = Member 모델의 data 값을 가지는 객체 가져오기
    member = Member.objects.get(**data)

    # 친구 데이터 받기
    data = {
        'member_email': 'zzanggu@naver.com',
        'member_password': 'zzzz'
    }

    # friend = Member 모델의 data 값을 가지는 객체 가져오기
    friend = Member.objects.get(**data)


    # 6번 1. 친구 삭제 (상태가 1인 친구들)
    # Fireds 모델 속 firends_objects 매니저에서 filter_member라는 메소드를 가져오기
    # member의 친구 목록에서 status가 True(=1, =승인)인 friend 친구의 값(친구 상태)을 가져오기
    friends = Friend.friends_objects.filter_member(member, status=True)
    # friends 반복하여 friend에 하나씩 담기
    for friend in friends:
        # 해당하는 친구의 status를 -1로 변경(친구 삭제)
        Friend.objects.filter(id=friend.id).update(status=-1)


    # 6번 2. 친구 거절 (상태가 0인 친구들)
    # Fireds 모델 속 firends_objects 매니저에서 filter_member라는 메소드를 가져오기
    # member의 친구 목록에서 status가 0(=대기)인 friend 친구의 값(친구 상태)을 가져오기
    friends = Friend.friends_objects.filter_member(member, status=0)
    # friends 반복하여 friend에 하나씩 담기
    for friend in friends:
        # 해당하는 친구의 status를 -1로 변경(친구 삭제)
        Friend.objects.filter(id=friend.id).update(status=-1)


    # 7번. 친구 수락
    # 받은 사람 정보 입력
    data = {
        'member_email': 'yuri@naver.com',
        'member_password': 'zzzz'
    }

    # 받는 사람 = Member 모델의 data 값을 가지는 객체 가져오기
    receiver = Member.objects.get(**data)

    # 보낸 사람 정보 입력
    data = {
        'member_email': 'zzanggu@naver.com',
        'member_password': 'zzzz'
    }

    # 보낸 사람 = Member 모델의 data 값을 가지는 객체 가져오기
    sender = Member.objects.get(**data)

    # Firend 모델에서 조건에 맞는 사람의 status를 True(=1 =승인)로 변경하기
    Friend.objects.filter(sender=sender, receiver=receiver, status=0).update(status=True)
