from django.db import models

from member.models import Member
from model.models import Period


class Cart(Period):
    member = models.ForeignKey(Member, on_delete=models.PROTECT, null=False)
    # 게시중 = 0, 결제 완료 = 1, 결제 취소 = -1, 삭제 = -2
    status = models.SmallIntegerField(null=False, default=0)

    class Meta:
        db_table = 'tbl_cart'
