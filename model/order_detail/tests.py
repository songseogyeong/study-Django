from django.test import TestCase

from member.models import Member
from order.models import Order


class OrderDetailTest(TestCase):
    # 1번. 로그인
    # 로그인 데이터 입력
    data = {
        'member_email': 'zzanggu@naver.com',
        'member_password': 'zzzz'
    }

    # member = Member 모델의 data 값을 가지는 객체를 조회하여 가져오기
    member = Member.enabled_objects.get(**data)


    # 2번. 주문내역(목록)
    # Order에서 로그인된 회원의 주문내역을 가져오기
    # enabled_objects 매니저를 통해 True(=결제 완료) 값만 가져오기
    # 값은 orders에 담기
    orders = Order.enabled_objects.filter(member=member)
    # orders 반복하여 order에 담기
    for order in orders:
        # order은 dict 형식으로 출력
        print(order.__dict__)


    # 3번. 주문 상세 내역(상세보기)
    # 데이터 입력
    data = {
        'id': 3,
    }

    # order의 아이디가 3번인 객체 가져와 order에 담기
    order = Order.objects.get(**data)
    # order에서 orderdetail을 역참조하여 모든 객체를 가져오고 order_items 담기
    order_items = order.orderdetail_set.all()

    # order_items 반복하여 order_item 담기:
    for order_item in order_items:
        # order_item의 product_sell_price(할인율) 출력
        print(order_item.product.product_sell_price)
        # order_item 출력
        print(order_item)
