from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=30, null=False, blank=False)
    product_price = models.IntegerField(null=False, blank=False)
    product_stock = models.IntegerField(null=False, blank=False)

    class Meta:
        db_table = 'tbl_product'
        ordering = ['-id']
