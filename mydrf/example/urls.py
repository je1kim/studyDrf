"""mydrf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include
from .views import HelloAPI, booksAPI, bookAPI, BooksAPI, BookAPI, BooksAPIMixins, BookAPIMixins, BooksAPIGenerics, BookAPIGenerics, BookViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     path('hello/', HelloAPI),
#     path('fbv/books/', booksAPI),                    # 함수형 뷰의 booksAPI 연결
#     path('fbv/book/<int:bid>', bookAPI),             # 함수형 뷰의 bookAPI 연결
#     path('cbv/books/', BooksAPI.as_view()),          # 클래스형 뷰의 BooksAPI 연결
#     path('cbv/book/<int:bid>', BookAPI.as_view()),   # 클래스형 뷰의 BookAPI 연결
#     path('mixins/books/', BooksAPIMixins.as_view()), 
#     path('mixins/book/<int:bid>', BookAPIMixins.as_view()), 
#     path('generics/books/', BooksAPIGenerics.as_view()), 
#     path('generics/book/<int:bid>', BookAPIGenerics.as_view()), 
# ]