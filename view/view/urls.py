"""
URL configuration for view project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from main.views import MainView
from view.views import StudentRegisterView, StudentResultView, StudentRegisterFormView, MemberRegisterFormView, \
    MemberRegisterView, MemberResultView, UserRegisterFromView, UserRegisterView, UserResultView, NumberInputFromView, \
    NumberInputView, NumberResultView, TextRegisterFromView, TextRegisterView, TextResultView, EventRegisterFormView, \
    EventRegisterView, EventResultView, NumRegisterFormView, NumRegisterView, NumResultView, ProductDetailView, ProductDetailAPI

urlpatterns = [
    # 기본 설정
    path('admin/', admin.site.urls),
    # include: 파일 속에 포함된 다른 템플릿을 가져오게 하기
    # member/ 로 시작하는 경로 뒤에 나머지 경로는 member.urls 파일 속에서 가져오기
    path('member/', include('member.urls')),
    # post/ 로 시작하는 경로 뒤에 나머지 경로는 post.urls 파일 속에서 가져오기
    path('post/', include('post.urls')),
    path('product/', include('product.urls')),
    path('products/', include('product.urls')),
    # 실습 1번. student
    # main 페이지의 경로는 '', as_view()를 사용하여 페이지 내에 MainView를 사용할 수 있게 한다.
    # as_view가 get이나 post를 담고 사용해준다.
    path('student/register/form/', StudentRegisterFormView.as_view(), name='student-register-form'),
    path('student/register/', StudentRegisterView.as_view(), name='student-register'),
    path('student/result/', StudentResultView.as_view(), name='student-result'),
    # 실습 2번. member
    path('member/register/form/', MemberRegisterFormView.as_view(), name='member-register-form'),
    path('member/register/', MemberRegisterView.as_view(), name='member-register'),
    path('member/result/', MemberResultView.as_view(), name='member-result'),
    # 실습 3번. user
    path('user/register/form/', UserRegisterFromView.as_view(), name='user-register-form'),
    path('user/register/', UserRegisterView.as_view(), name='user-register'),
    path('user/result/', UserResultView.as_view(), name='user-result'),
    # 실습 4번. number
    path('number/input/form/', NumberInputFromView.as_view(), name='number-input'),
    path('number/input/', NumberInputView.as_view(), name='number-input'),
    path('number/result/', NumberResultView.as_view(), name='number-result'),
    # 실습 5번. text
    path('text/register/form/', TextRegisterFromView.as_view(), name='text-register-form'),
    path('text/register/', TextRegisterView.as_view(), name='text-register'),
    path('text/result/', TextResultView.as_view(), name='text-result'),
    # 실습 6번. event
    path('event/register/form/', EventRegisterFormView.as_view(), name='event-register-form'),
    path('event/register/', EventRegisterView.as_view(), name='event-register'),
    path('event/result/', EventResultView.as_view(), name='event-result'),
    # 실습 7번. num
    path('num/register/form/', NumRegisterFormView.as_view(), name='event-register-form'),
    path('num/register/', NumRegisterView.as_view(), name='event-register'),
    path('num/result/', NumResultView.as_view(), name='event-result'),
    # 실습 8번. rest
    path('product/product/', ProductDetailView.as_view(), name='product'),
    path('products/<int:product_id>/', ProductDetailAPI.as_view(), name='product-api'),
    # 메인화면
    path('', MainView.as_view()),
]
