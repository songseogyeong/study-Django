from django.db import models

from alarm.managers import AlarmManager
from member.models import Member
from model.models import Period
from post.models import Post


class Alarm(Period):
    sender = models.ForeignKey(Member, null=False, related_name='sender', on_delete=models.PROTECT)
    receiver = models.ForeignKey(Member, null=False, related_name='receiver', on_delete=models.PROTECT)
    post = models.ForeignKey(Post, null=False, on_delete=models.PROTECT)
    # 0: 안읽음, 1: 읽음, -1: 삭제
    status = models.SmallIntegerField(default=0)

    objects = models.Manager()
    enabled_objects = AlarmManager()

    class Meta:
        db_table = 'tbl_alarm'
        ordering = ['-id']
