from django.db import models
from model.models import Period



class Member(Period):
    member_email = models.CharField(blank=False, null=False, max_length=50)
    member_password = models.CharField(blank=False, null=False, max_length=20)
    member_name = models.TextField(blank=False, null=False)
    member_age = models.IntegerField(null=False, default=0)
    # 일반 회원: True, 관리자: False
    member_status = models.BooleanField(null=False, default=True)
    # 정상 회원: True, 탈퇴 회원: False
    status = models.BooleanField(null=False, default=True)

    class Meta:
        db_table = 'tbl_member'


