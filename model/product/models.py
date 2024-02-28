from django.db import models

from model.models import Period
from product.managers import ProductManager


class Product(Period):
    product_name = models.TextField(null=False, blank=False)
    product_price = models.BigIntegerField(null=False, blank=False)
    product_discount = models.SmallIntegerField(null=False, blank=False, default=0)
    # 판미중 = True, 판매 중지 = False
    status = models.BooleanField(null=False, default=False)
    # objects = models.Manager() 먼저 작성
    # objects = models.Manager()는 기본 매니저를 정의한 것이기 때문이다.
    objects = models.Manager()
    # 사용자 정의 매니저
    sell_price_objects = ProductManager()

    class Meta:
        db_table = 'tbl_product'
        # 다른 객체에서 참조로 Product에 접근할 때, 사용할 manager 설정
        base_manager_name = 'sell_price_objects'
