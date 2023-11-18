
from rest_framework import serializers
from .models import Todo

"""
   Todo 목록 조회 시리얼라이저
"""
class TodoSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Todo
        fields = ('id', 'title', 'complete', 'important')

"""
  상세 조회용 Todo 시리얼라이저
"""
class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Todo
        fields = ('id', 'title', 'description', 'created', 'complete', 'important')

"""
    생성용 Todo 시리얼라이즈
"""
class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Todo
        fields = ('title', 'description', 'important')