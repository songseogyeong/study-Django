import datetime
import math

from django.db.models import F
from django.db.models.functions import Floor
from django.test import TestCase
from django.utils import timezone

from product.models import Product


class ProductTestCase(TestCase):
    # 1번. 상품 추가
    # 추가될 상품 목록을 datas에 받기
    datas = [
        Product(product_name='춘천 국물 닭갈비', product_price=13_200, product_discount=15),
        Product(product_name='노르웨이 생연어', product_price=17_900, product_discount=20),
        Product(product_name='성주 참외', product_price=25_900, product_discount=11),
        Product(product_name='간편 미식 도시락', product_price=5_200, product_discount=20),
    ]

    # Product 모델 속 필드에 datas 값 추가
    # 여러개의 객체를 추가하기 때문에 bulk_create 사용
    Product.objects.bulk_create(datas)


    # 2번. 상품 게시
    # Product 모델 속 모든 객체의 상태를 True(=판매중)로 변경
    Product.objects.all().update(status=True)


    # 3번. 상품 할인율 적용 가격
    # Product의 모든 객체 가져오기(enabled_objects 매니저 = True 값만 가져오기 = 팬매중인 상품만 가져오기)
    # 할인율 적용 연산(Floor 함수 사용) 후 product_sell_price 별칭 지정
    # 값은 products 담기
    products = Product.enabled_objects.all().annotate(product_sell_price=Floor(F('product_price') * (1 - F('product_discount') / 100) / 10) * 10)
    # products 반복하여 product 담기:
    for product in products:
        # products의 가격, 할인율, 적용된 가격 출력
        print(product.product_price, product.product_discount, product.product_sell_price)


    # 4번. 상품 수정
    # 조건에 맞는 객체를 가져와 가격을 수정하고, 수정 시간을 현재 시간으로 설정
    Product.objects.filter(id=3).update(product_price=25000, updated_date=timezone.now())


    # 5번. 상품 목록
    # Product 모델 속 모든 객체의 값을 출력하기
    print(Product.objects.all().values)
