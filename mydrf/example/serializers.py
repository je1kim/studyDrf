from rest_framework import serializers
from .models import Book

# class BookSerializer(serializers.Serializer):
#     bid            = models.IntegerField(primary_key=True)   # 책 ID
#     title          = models.CharField(max_length=50)         # 책 제목
#     author         = models.CharField(max_length=50)         # 저자
#     category       = models.CharField(max_length=50)         # 카테고리
#     pages          = models.IntegerField()                   # 페이지 수
#     price          = models.IntegerField()                   # 가격
#     published_date = models.DateField()                      # 출판일
#     decription     = models.TextField()                      # 도서 설명

#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)
    
#     def update(self, intance, validated_data):
#         instance.bid            = validated_data.get('bid', instance.bid)
#         instance.title          = valudated_data.get('title', instance.title)
#         instance.author         = valudated_data.get('author', instance.author)
#         instance.category       = valudated_data.get('category', instance.category)
#         instance.pages          = valudated_data.get('pages', instance.pages)
#         instance.price          = valudated_data.get('price', instance.price)
#         instance.published_date = valudated_data.get('published_date', instance.published_date)
#         instance.decription     = valudated_data.get('decription', instance.decription)
#         instance.save()

#         return instance

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Book
        fields = ['bid', 'title', 'author', 'category', 'pages', 'price', 'published_date', 'description']