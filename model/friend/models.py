from django.db import models
from django.db.models import Q, F

from member.models import Member
from model.models import Period

# 친구 목록
# FriendManager 정의:
class FriendManager(models.Manager):
    # filter_member 메소드 정의:
    def filter_member(self, member, **kwargs):
        # condition_sender: Q 객체를 사용하여 sender 필드가 주어진 member와 동일하게 하기
        condition_sender = Q(sender=member)
        # condition_receiver: Q 객체를 사용하여 receiver 필드가 주어진 member와 동일하게 하기
        condition_receiver = Q(receiver=member)

        # friends_receiver: Friend(부모) 객체의 receiver 값을 조건에 맞게 가져오기, receiver 필드는 friend로 별칭 지정
        friends_receiver = super().get_queryset().annotate(friend=F('receiver')).filter(condition_sender, **kwargs)
        # friends_sender: Friend(부모) 객체의 sender 값을 조건에 맞게 가져오기, sender 필드는 friend로 별칭 지정
        friends_sender = super().get_queryset().annotate(friend=F('sender')).filter(condition_receiver, **kwargs)

        # friends: union(합집합)을 사용하여 friends_sender와 friends_receiver 합치기
        friends = friends_sender.union(friends_receiver)
        # 리턴 값 설정
        return friends


class Friend(Period):
    FRIEND_STATUS = [
        (-1, '거절'),
        (0, '대기'),
        (1, '승인')
    ]

    sender = models.ForeignKey(Member, related_name='sender_set', null=False, on_delete=models.PROTECT)
    receiver = models.ForeignKey(Member, related_name='receiver_set', null=False, on_delete=models.PROTECT)
    status = models.SmallIntegerField(choices=FRIEND_STATUS, default=0)
    objects = models.Manager()
    friends_objects = FriendManager()

    class Meta:
        db_table = 'tbl_friend'
