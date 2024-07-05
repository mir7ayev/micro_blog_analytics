from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import (
    PostView, UserVisit,
)


class PostViewSerializer(ModelSerializer):
    class Meta:
        model = PostView
        fields = '__all__'


class UserVisitSerializer(ModelSerializer):
    class Meta:
        model = UserVisit
        fields = '__all__'
