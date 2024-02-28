from django.db import transaction
from django.test import TestCase

from cart.models import Cart
from cart_detail.models import CartDetail
from member.models import Member
from product.models import Product


class CartTests(TestCase):
    # 1번. 로그인
    # 로그인 데이터 입력
    data = {
        'member_email': 'zzanggu@naver.com',
        'member_password': 'zzzz'
    }

    # member = Member 모델의 data 값을 가지는 객체를 조회하여 가져오기
    member = Member.enabled_objects.get(**data)


    # 2번. 상품 목록
    # Product 모델의 모든 객체 가져오기
    products = Product.sell_price_objects.all()


    # 3번. 상품 상세페이지
    # products 3번 인덱스 값을 가져와 product에 담기
    product = products[3]
    # print(product.__dict__)


    # 4번. 장바구니에 상품 추가
    # 4번 1. 내 장바구니 가져오기
    # Cart 모델에서 status 필드가 0이고, member 필드가 meber인 객체를 가져와 my_cart에 담기
    my_cart = Cart.objects.filter(status=0, member=member)

    # 장바구니가 없을 때, (장바구니에 상품이 하나도 없을 때)
    if not my_cart.exists():
        # 해당하는 member의 새로운 장바구니를 만들어서 my_cart에 담기
        my_cart = Cart.objects.create(member=member)

    # 장바구니가 존재할 때, (장바구니에 추가된 다른 상품이 존재할 때)
    else:
        # 기존 장바구니를 my_cart에 담기
        my_cart = my_cart.first()

    # CartDetail 모델에서 cart 필드가 my_cart, product 필드가 product, quantity(개수) 3개인 값을 가지는 객체 생성
    CartDetail.objects.create(cart=my_cart, product=product, quantity=3)


    # 실습 1번
    # 장바구니 목록
    # 상품 정보, 수량

    # 실습 1번 1. 로그인
    # 로그인 정보 담기
    data = {
        'member_email': 'zzanggu@naver.com',
        'member_password': 'zzzz'
    }

    # member = Member 모델의 data 값을 가지는 객체를 조회하여 가져오기
    member = Member.enabled_objects.get(**data)

    # 실습 1번 2. 내 장바구니에 있는 상품 정보, 수량 가져오기
    # CartDetail 모델에서 조건에 맞는 product 정보 조회
    # 조건: 장바구니 내 항목과 로그인된 회원의 장바구니가 결제 전 상태인 product를 가져와 carts에 담기
    carts = CartDetail.objects.select_related('product').filter(status=0, cart=Cart.objects.filter(status=0, member=member))
    # carts 반복하여 cart에 하나씩 담기
    for cart in carts:
        # cart의 product를 dict 형식으로 출력
        print(cart.product.__dict__)
        # cart의 가격 출력
        print(cart.quantity)


    # 실습 2번
    # 장바구니에 담긴 상품 임의로 삭제

    # 트랜잭션 지원 (오류잡기)
    # 오류 발생 시 자동 롤백을 위해 사용하고 오류가 없으면 커밋된다.
    # try 사용 시 한계가 존재한다. (delete 시 다시 생성해도 id 값이 달라지는 문제...)
    # django에서는 트랜잭션을 지원하기 때문에,
    # transaction.atomic을 사용하여 오류 발생 시 쿼리가 실행되지 않고 자동 롤백이 되도록 잡을 수 있다.

    # ① with transaction.atomic():
    # with문 사용 이유: 자동으로 닫아주기 위해서 사용
    # 전체 쿼리 중 일부분에만 사용이 가능하다.
    # 블록 전체를 하나의 트랜잭션으로 설정

    # 2번
    # service 함수 사용 할때 문제 생기면 transaction.actomic이 잡아줌
    # 메소드 위에 데코레이터로 걸어주기
    # 메소드 전체를 하나의 트랜잭션으로 설정
    @transaction.atomic
    def service(self):
        data = {
            'member_email': 'zzanggu@naver.com',
            'member_password': 'zzzz'
        }

        member = Member.enabled_objects.get(**data)

        my_cart = Cart.objects.get(member=member, status=0)

        carts = CartDetail.objects.filter(status=0, cart=my_cart)
        cart = carts[0]
        cart.status = -1
        carts.save(update_fields=['status'])

        if not CartDetail.objects.filter(my_cart=my_cart, status=0).exists():
            my_cart.status = -2
            my_cart.save(update_fields=['status'])