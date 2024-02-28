from datetime import datetime

from django.db.models import Q
from django.test import TestCase

from image.models import Image
from member.models import Member
from random import randint


# 실습 2번.
# 필드명
# id, created_date, updated_date, image_name, image_link, status, member_id

class ImageTestClass(TestCase):
    # 실습 2번 1.
    # 프로필 이미지는 여려개 생성 될 수 있다고 가정 하고 member_id는 랜덤으로 입력 하기
    # 이미지 이름 i default=1 번째 부터 100번째 까지 이미지 생성

    # list 초깃값을 가지는 images 변수 선언
    images = []

    # Member 모델 속 객체를 모두 가져오고 members_queryset 담기
    members_queryset = Member.objects.all()

    # 100번 반복하여 i에 하나씩 담기
    for i in range(100):
        # image 데이터 입력
        # image_name: i + 1 (0 + 1 = 1, 1 + 1 = 2 ... 99 + 1 = 100)
        # member: member를 랜덤으로 넣기(0부터 시작해서 member 수 - 1 까지 중 숫자 랜덤)
        # members_queryset 인덱스 번호 값으로 객체를 가져오는데, 인덱스 번호가 0부터 시작하기 때문에 -1 해준다.
        image = {
            'image_name': i + 1,
            'member': members_queryset[randint(0, len(members_queryset) -1)],
        }
        # images에 image 값 추가
        # dict 객체이기 때문에 Image 객체로 감싸서 값을 추가해야 한다.
        images.append(Image(**image))

    # images 생성하여 테이블에 저장
    Image.objects.bulk_create(images)


    # 실습 2번 2.
    # 생성 날짜가 2월 21일 16시 이후, 사용자 id 가 x 번째 사용자 일 때 해당 프로필 사진 조회
    # 만든 서비스 전체 fake를 이용해서 삭제 => 완성 후 수업에 지장이 없게 원상 복구

    # search_time에 datetime 메소드를 사용하여 2월 21일 16시 값을 담기
    search_time = datetime(2024, 2, 21, 16, 00)
    # condition1 = member 모델 속 id 객체가 5인 조건
    condition1 = Q(member__id=5)
    # condition2 = created_date 객체가 search_time 이후인 조건
    condition2 = Q(created_date__gt=search_time)
    # Image 모델 속 객체를 해당하는 조건에 맞춰 image_link 필드의 값만 가져와 image_list에 담기
    image_list = Image.objects.filter(condition1 & condition2).values('image_link')

    # image_list 반복하여 image 하나씩 담기:
    for image in image_list:
        # image 출력
        print(image)
