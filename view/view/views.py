from random import randint

from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView


# 실습 1번. student
# 학생의 번호, 국어, 영어, 수학 점수를 전달받은 뒤
# 총점과 평균을 화면에 출력한다.

# form태그는 get방식을 사용한다.
# 출력 화면에서 다시 입력화면으로 돌아갈 수 있게 한다.

# 입력: task/student/register.html
# 출력: task/student/result.html

class StudentRegisterFormView(View):
    def get(self, request):
        return render(request, 'task/student/register.html')


class StudentRegisterView(View):
    def get(self, request):
        data = request.GET
        data = {
            'id': data['id'],
            'kor': int(data['kor']),
            'eng': int(data['eng']),
            'math': int(data['math'])
        }

        total = data['kor'] + data['eng'] + data['math']
        average = round(total / 3, 2)

        return redirect(f'/student/result?total={total}&average={average}')


class StudentResultView(View):
    def get(self, request):
        data = request.GET
        context = {
            'total': request.GET['total'],
            'average': request.GET['average']
        }
        print(context)
        return render(request, 'task/student/result.html', context)



        # 리다이렉트로 데이터 넘기는 방법
        # url에 데이터 심기-뷰에 넘길때
        # 쿼리스트링으로 담아가기-뷰에 넘길때
        # 화면에서 쓸 거면 섹션을 사용-화면으로 넘길때


# 실습 2번. member
# 회원의 이름과 나이를 전달받는다.
# 전달받은 이름과 나이를 아래와 같은 형식으로 변경시킨다.
# "홍길동님은 20살!"
# 결과 화면으로 이동한다.

# 이름과 나이 작성: task/member/register.html
# 결과 출력: task/member/result.html

class MemberRegisterFormView(View):
    def get(self, request):
        return render(request, 'task/member/register.html')


class MemberRegisterView(View):
    def get(self, request):
        data = request.GET
        data = {
            'name': data['name'],
            'age': data['age']
        }
        result = f'{data["name"]}님은 {data["age"]}살!'
        return redirect(f'/member/result?result={result}')

    def post(self, request):
        data = request.POST
        data = {
            'name': data['name'],
            'age': data['age']
        }
        result = f'{data["name"]}님은 {data["age"]}살!'
        return redirect(f'/member/result?result={result}')

class MemberResultView(View):
    def get(self, request):
        result = request.GET['result']

        return render(request, 'task/member/result.html', {'result': result})


# 실습 3번. user
# 회원의 이름과 나이를 전달 받은 후,
# 20살 미만이면 "지원님은 미성년자 입니다"
# 20살 이상이면 "지원님은 성인이시군요!"
# 결과 화면에 문구 출력하기

# 작성: task/user/register.html
# 출력: task/user/result.html

class UserRegisterFromView(View):
    def get(self, request):
        return render(request, 'task/user/register.html')

class UserRegisterView(View):
    def get(self, request):
        data = request.GET
        data = {
            'name': request.GET['name'],
            'age': int(request.GET['age'])
        }
        name = data['name']
        age = data['age']

        if age > 21:
            result = f'{name}님은 성인이시군요!'

        else:
            result = f'{name}은 미성년자 입니다'

        return redirect(f'/user/result/?result={result}')


class UserResultView(View):
    def get(self, request):
        result = request.GET['result']

        return render(request, 'task/user/result.html', {'result': result})


# 실습 4번. number
# 1~10사이의 숫자를 입력받아(input[type=number])
# 뷰에서 1~10사이의 랜덤한 숫자(random.randint())를 생성한 후
# 일치할 경우 "축하합니다! 정답입니다!"를 화면으로,
# 불일치할 경우 차이(절댓값)를 "아쉽네요... 정답과 [차이]만큼 차이가 나요!" 출력하기

# 작성: task/number/input.html
# 출력: task/number/result.html

class NumberInputFromView(View):
    def get(self, request):
        return render(request, 'task/number/input.html')

class NumberInputView(View):
    def get(self, request):
        data = request.GET
        number = int(data['number'])
        random = randint(0, 10)
        absolute = abs(random - number)
        print(random)

        if number == random:
            result = '축하합니다! 정답입니다!'
        else:
            result = f'아쉽네요... 정답과 {absolute}만큼 차이가 나요!'

        return redirect(f'/number/result/?result={result}')

class NumberResultView(View):
    def get(self, request):
        result = request.GET['result']

        return render(request, 'task/number/result.html', {'result': result})


# 실습 5번. text
# 사용자에게 영문 텍스트를 입력 받은 후
# 대문자를 소문자로 소문자를 대문자로 출력하기

# 작성: task/text/register.html
# 출력: task/text/result.html
class TextRegisterFromView(View):
    def get(self, request):
        return render(request, 'task/text/register.html')

class TextRegisterView(View):
    def get(self, request):
        text = request.GET['text']

        result = text.swapcase()

        return redirect(f'/text/result/?result={result}')

class TextResultView(View):
    def get(self, request):
        result = request.GET['result']

        return render(request, 'task/text/result.html', {'result': result})


# 실습 6번. event
# 회원의 이름 /제목/ 내용을 받고
# (이름)회원님이 (제목)이라는 주제의 이벤트를 만들었어요!
# (내용)하실분~~
# 이라는 내용 출력하기

# 작성: task/event/register.html
# 출력: task/event/result.html
class EventRegisterFormView(View):
    def get(self, request):
        return render(request, 'task/event/register.html')

class EventRegisterView(View):
    def get(self, request):
        name = request.GET.get('name')
        title = request.GET.get('title')
        content = request.GET.get('content')


        result = f'{name} 회원님이 {title}이라는 주제의 이벤트를 만들었어요!</br>{content} 하실 분~~'

        return redirect(f'/event/result/?result={result}')

class EventResultView(View):
    def get(self, request):
        result = request.GET['result']

        return render(request, 'task/event/result.html', {'result': result})


# 실습 7. num
# 사용자에게 숫자를 입력 받기
# 입력 받은 숫자는 몇 자리 숫자인지 출력하기
# 출력 예시: [입력한 숫자]는 N의 자리 입니다~!

# 작성: task/num/register.html
# 출력: task/num/result.html

class NumRegisterFormView(View):
    def get(self, request):
        return render(request, 'task/num/register.html')

class NumRegisterView(View):
    def get(self, request):
        num = int(request.GET['num'])
        realnum = request.GET['num']

        count = 0

        while num != 0:
            num = num // 10
            count += 1

        result = {
            'count': count,
            'realnum': realnum
        }

        return redirect(f'/num/result/?count={count}&realnum={realnum}')


class NumResultView(View):
    def get(self, request):
        context = {
            'count': request.GET['count'],
            'realnum': request.GET['realnum']
        }


        return render(request, 'task/num/result.html', context)


# 실습 8번. rest
# 상품 정보
# 번호, 상품명, 가격, 재고
# 상품 1개 정보를 REST 방식으로 설계한 뒤
# 화면에 출력하기
# product/1
# task/product/product.html
# 데이터 받고 오기

# 1. 페이지 이동
class ProductDetailView(View):
    def get(self, request):
        return render(request, 'task/product/product.html')


class ProductDetailAPI(APIView):
    def get(self, request, product_id):
        # 데이터 받기
        data = {
            'id': product_id,
            'product_name': '사과',
            'product_price': 5000,
            'product_stock': 50,
        }

        return Response(data)





