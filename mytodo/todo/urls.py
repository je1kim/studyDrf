"""mytodo URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name="todo_list"),
    path('<int:pk>/', views.todo_detail, name="todo_detail"),
    path('post/', views.todo_post, name="todo_post"),
    path('<int:pk>/edit/', views.todo_edit, name="todo_edit"),
    path('done/', views.done_list, name="done_list"),
    path('done/<int:pk>/', views.todo_done, name="todo_done"),
]
