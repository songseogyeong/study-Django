from django.db import transaction
from django.test import TestCase

from alarm.models import Alarm
from member.models import Member
from post.models import Post
from reply.models import Reply


class AlarmTestCase(TestCase):
    with transaction.atomic():
        # 1번. 로그인
        # 로그인 데이터 입력
        data = {
            'member_email': 'zzanggu@naver.com',
            'member_password': 'zzzz'
        }

        # member = Member 모델의 data 값을 가지는 객체를 조회하여 가져오기
        member = Member.objects.get(**data)


        # 2번. 게시글 목록
        posts = Post.objects.all()[0:10]


        # 3번. 게시글 상세보기
        post = Post.objects.get(id=posts[0].id)


        # 4번. 댓글 작성
        data = {
            'reply_content': '테스트 댓글10',
            'post': post,
            'member': member
        }

        reply = Reply.objects.create(**data)
        reply.group_id = reply.id
        reply.save(update_fields=['group_id'])


        # 5번. 알람 추가
        data = {
            'receiver': post.member,
            'sender': member,
            'post': post
        }

        Alarm.objects.create(**data)

        # 6번. 알람 목록
        # 6번 1. 로그인
        # 로그인 데이터 입력
        data = {
            'member_email': 'zzanggu@naver.com',
            'member_password': 'zzzz'
        }

        # member = Member 모델의 data 값을 가지는 객체를 조회하여 가져오기
        member = Member.objects.get(**data)

        # 6번 2. 알람 목록
        alarms = Alarm.enabled_objects.filter(receiver=member).values()
        for alarm in alarms:
            print(alarm)

        # 7번. 알람 확인
        data = {
            'id': 2
        }

        # 업데이트는 filter 쿼리셋에 사용가능
        count = Alarm.enabled_objects.filter(**data).update(status=1)
        print(count)
