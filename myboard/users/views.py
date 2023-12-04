from django.shortcuts import render

# Create your views here.
"""

    회원가입의 경우 POST, 즉 회원 생성 기능만 있기 때문에 
    굳이 ViewSet을 사용해 다른 API 요청을 처리해줄 필요가 없음

    이 때문에 회원가입 기능은 generics의 CreateAPIView를 사용해 작성

"""

from django.contrib.auth.models import User
from rest_framework import generics

from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView): # CreateAPIView(generics) 사용 구현
    queryset         = User.objects.all()
    serializer_class = RegisterSerializer