from django.db import models

from member.models import Member
from model.models import Period


class Order(Period):
    member = models.ForeignKey(Member, on_delete=models.PROTECT, null=False)
    payment = models.TextField(null=False, blank=False)
    price = models.BigIntegerField(null=False)
    delivery_address = models.TextField(null=False, blank=False)
    # 결제 완료 = True, 결제 취소 = False
    status = models.BooleanField(null=False, default=True)

    class Meta:
        db_table = 'tbl_order'
        ordering = ['-id']
