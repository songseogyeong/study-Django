from django.db import transaction
from django.db.models import Sum, F
from django.test import TestCase
from django.utils import timezone

from cart.models import Cart
from cart_detail.models import CartDetail
from member.models import Member
from order.models import Order
from order_detail.models import OrderDetail
from product.models import Product


class OrderTests(TestCase):
    # 1번. 로그인
    # 로그인 데이터 입력
    data = {
        'member_email': 'zzanggu@naver.com',
        'member_password': 'zzzz'
    }

    # member = Member 모델의 data 값을 가지는 객체를 조회하여 가져오기
    member = Member.enabled_objects.get(**data)


    # 2번. 장바구니 결제
    with transaction.atomic():
        # 2번 1. 장바구니 가져오기
        # 장바구니에서 결제할 항목 선택하기
        data = {
            'ids': [1, 2, 3]
        }

        # Cart 모델에서 status 필드가 0이고, member 필드가 meber인 객체를 가져와 my_cart에 담기
        my_cart = Cart.objects.get(status=0, member=member, id__in=data['ids'])
        # CartDetail 모델에서 cart=my_cart, status=0(=게시중) 조건을 가지는 객체를 cart_items에 담기
        cart_items = CartDetail.objects.filter(cart=my_cart, status=0)


        # 2번 2. 전체 가격 구하기
        # 초깃값을 가지는 pirce 선언
        price = 0
        # cart_items 반복하여 cart_item 하나씩 담기
        for cart_item in cart_items:
            # cart_items 상품의 할인율이 적용된 가격에 상품 개수를 곱해 총 금액을 구하기
            # 상품별 총 합계는 pirce에 하나씩 더해주기(결제 금액)
            price += cart_item.product.product_sell_price * cart_item.quantity


        # 2번 3. 결제
        # 결제 데이터 담기
        data = {
            'member': member,
            'payment': 'card',
            'price': price,
            'delivery_address': '경기도 남양주시',
        }

        # data 값을 가지는 객체를 생성하고 order에 담기
        order = Order.objects.create(**data)

        # cart_items 반복하여 cart_item 하나씩 담기
        for cart_item in cart_items:
            # OrderDetail 모델 속 객체 생성 후 테이블에 값 저장하기
            OrderDetail.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity)

            # 결제 후 장바구니 속 상품 상태 업데이트(상태=결제 완료, 수정 시간=현재 시간)
            cart_item.status = 1
            cart_item.updated_date = timezone.now()
            cart_item.save(update_fields=['status', 'updated_date'])

            # 결제 후 장바구니 상태 업데이트
            # 만약, 장바구니 항목에 게시 중이 값이 없다면:
            # exists() 사용해 값이 있으면 True, 없으면 False
            # not 붙여 False 값을 찾는다.
            if not CartDetail.objects.filter(cart=my_cart, status=0).exists():
                # 게시 중인 장바구니 항목이 없으면 장바구니 상태 업데이트(상태=결제 완료, 수정 시간=현재 시간)
                my_cart.status = 1
                my_cart.updated_date = timezone.now()
                my_cart.save(update_fields=['status', 'updated_date'])


    # 3번. 상품을 직접 결제
    # 3번 1. 로그인
    # 로그인 데이터 입력
    data = {
        'member_email': 'zzanggu@naver.com',
        'member_password': 'zzzz'
    }

    # member = Member 모델의 data 값을 가지는 객체를 조회하여 가져오기
    member = Member.enabled_objects.get(**data)


    # 3번 2. 상품 목록
    # Product 모델 속 객체 가져오기
    products = Product.sell_price_objects.all()


    # 3번 3. 상품 상세 보기
    # 상품 데이터 입력
    data = {
        'id': 2
    }

    # id=2 조건을 가지는 객체 가져오고 product에 담기
    product = Product.sell_price_objects.get(**data)


    # 3번 3. 상품과 수량 선택
    # 결제 데이터 입력
    data = {
        'member': member,
        'payment': 'kakaopay',
        'price': product.product_sell_price_objects * 5,
        'delivery_address': '서울시 강남구'
    }

    # 입력된 결제 데이터로 order 객체 생성
    order = Order.objects.create(**data)


    # 3번 4. 결제
    # 결제 상세 데이터 입력
    data = {
        'product': product,
        'quantity': 5
    }

    # 입력된 결제 상세 데이터로 orderdetail 객체 생성
    OrderDetail.objects.create(order=order, **data)


    # 4번. 결제 취소
    # 주문 데이터 입력
    data = {
        'id': 2,
    }

    # 해당하는 주문 객체 가져와서 주문 취소로 상태 업데이트 하기(상태=결제 취소, 수정 시간=현재 시간)
    order = Order.enabled_objects.get(id=2)
    order.status = False
    order.updated_date = timezone.now()
    order.save(update_field=['status', 'updated_date'])
