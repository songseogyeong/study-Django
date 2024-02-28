from django.db import models

from member.models import Member
from model.models import Period

# 실습 1번.
# image 프로필 서비스 저장 서비스 1개 제작
# tip. member id 외래키, 이미지 절대경로 1개(default = /images/) , 이미지 이름 1개(컬럼), 날짜, status (컬럼)으로 서비스 생성

class Image(Period):
    member = models.ForeignKey(Member, null=False, on_delete=models.PROTECT)
    image_name = models.CharField(blank=False, null=False, max_length=20)
    image_link = models.TextField(blank=False, null=False, default='/images/')
    status = models.BooleanField(null=False, default=True)

    class Meta:
        db_table = 'tbl_image'
        ordering = ['-id']
