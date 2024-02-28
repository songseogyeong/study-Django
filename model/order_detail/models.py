from django.db import models

from model.models import Period
from order.models import Order
from product.models import Product


class OrderDetail(Period):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False)
    quantity = models.IntegerField(null=False, default=1)

    class Meta:
        db_table = 'tbl_order_detail'
        ordering = ['-id']

