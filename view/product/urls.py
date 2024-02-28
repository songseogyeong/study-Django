from django.contrib import admin
from django.urls import path, include

from main.views import MainView
from product.views import ProductDetailView, ProductDetailAPI

app_name = 'product'

urlpatterns = [
    path('product/', ProductDetailView.as_view(), name='product'),
    path('<int:product_id>/', ProductDetailAPI.as_view(), name='product-api'),
]
