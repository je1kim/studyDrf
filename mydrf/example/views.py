from django.shortcuts import render

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404 

from .models import Book                    # 모델 불러오기
from .serializers import BookSerializer     # 시리얼라이저 불러오기

# Create your views here.
"""
 @ DRF FBV, CBV, API view
  - FBV(Function Based View) : 함수기반 views
  - CBV(Class Based View) : 클래스 기반 뷰
    => 아주 기본척인 형태에서 다양한 방법으로 확정될 수 있다는 장점이 있음

예시:
class HelloAPI(APIView) : # CBV 기반 API view
    def get(self, request):
        return Response("hello world")

  - FBV와 CBV의 성능의 큰 차이는 없음
"""
@api_view(['GET'])      # FBV 기반 API views
def HelloAPI(request):
    return Response("hello world!")

@api_view(['GET', 'POST'])
def booksAPI(request):
    if request.method == 'GET':
        books      = Book.objects.all()                                # Book 모델로부터 전체 데이터 가져오기
        serializer = BookSerializer(books, many=True)                  # 시리얼라이저에 전체 데이터를 한번에 집어넣기(직렬화, many=True) -> many 옵션은 여러 데이터 처리 허용
        return Response(serializer.data, status=status.HTTP_200_OK)    # resturn Response

    elif request.method == "POST":                                     # POST 요청(도서정보 등록)
        serializer = BookSerializer(data=request.data)                 # POST 요청으로 들어온 데이터를 시리얼라이저에 집어넣기
        if serializer.is_valid():                                      # 데이터 유효성 확인
            serializer.save()                                          # 시리얼라이저의 역직렬화를 통해 save(), 모델시리얼라이저의 기본 create() 함수가 동작
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # 201 메시지를 보내며 성공
         
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 404 잘못된 요청

@api_view(['GET'])
def bookAPI(request, bid): # /book/bid
    book       = get_object_or_404(Book, bid=bid)                 # bid=id인 데이터를 Book에서 가져오고, 없으면 404에러
    serializer = BookSerializer(book)                             # 시리얼라이즈에 데이터 집어넣기(질렬화)
    return Response(serializer.data, status=status.HTTP_200_OK)   # return Response!

"""

  위 코드를 CBV 로 변환

"""


class BooksAPI(APIView):
    def get(self, request):
        books      = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookAPI(APIView):
    def get(self, request, bid):
        book       = get_object_or_404(Book, bid=bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
