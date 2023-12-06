from django.shortcuts import render

# Create your views here.
"""

    회원가입의 경우 POST, 즉 회원 생성 기능만 있기 때문에 
    굳이 ViewSet을 사용해 다른 API 요청을 처리해줄 필요가 없음

    이 때문에 회원가입 기능은 generics의 CreateAPIView를 사용해 작성

"""

from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        print(request)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token      = serializer.validated_data  # validate() 의 리턴값인 Token 을 받아옴
        return Response({"token": token.key}, status=status.HTTP_200_OK)

class RegisterView(generics.CreateAPIView): # CreateAPIView(generics) 사용 구현
    queryset         = User.objects.all()
    serializer_class = RegisterSerializer

