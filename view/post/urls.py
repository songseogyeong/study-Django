from django.contrib import admin
from django.urls import path, include

from post.views import PostListView, PostWriteView, PostDetailView, PostUpdateView, PostDeleteView, PostListAPI

app_name = 'post'

urlpatterns = [
    path('write/', PostWriteView.as_view(), name='write'),
    # 경로에 데이터를 저장하고 싶다면 <>를 열어서 타입과, 어떤 값을 담을지 정확하게 작성
    path('detail/', PostDetailView.as_view(), name='detail'),
    path('update/', PostUpdateView.as_view(), name='update'),
    path('delete/', PostDeleteView.as_view(), name='delete'),
    # list페이지 이동
    path('list/', PostListView.as_view(), name='list'),
    # list 경로 가져오기
    path('list/<int:page>/', PostListAPI.as_view(), name='list-api'),
]
