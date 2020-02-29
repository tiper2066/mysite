from django.urls import path
from . import views     # views.py 의 모든것

urlpatterns = [     # url 경로 설정
    path('', views.index, name='index'),   # polls/의 root 접속시 index 함수호출
]