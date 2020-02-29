from django.shortcuts import render
from django.http import HttpResponse

# 응답 메시지 함수
def index(request):
    return HttpResponse("Hello, world")