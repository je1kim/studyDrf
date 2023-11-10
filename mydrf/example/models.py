from django.db import models

# Create your models here.
class Book(models.Model):
    bid            = models.IntegerField(primary_key=True)   # 책 ID
    title          = models.CharField(max_length=50)         # 책 제목
    authoer        = models.CharField(max_length=50)         # 저자
    category       = models.CharField(max_length=50)         # 카테고리
    pages          = models.IntegerField()                   # 페이지 수
    price          = models.IntegerField()                   # 가격
    published_date = models.DateField()                      # 출판일
    decription     = models.TextField()                      # 도서 설명
    