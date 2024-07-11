from rest_framework.serializers import ModelSerializer
from .models import (
    PostView, PostViewByUser, PostViewByAge, PostViewByCountry,
    PostViewByGender,
)


class PostViewByGenderSerializer(ModelSerializer):
    class Meta:
        model = PostViewByGender
        fields = ('post_id', 'gender', 'count')


class PostViewByAgeSerializer(ModelSerializer):
    class Meta:
        model = PostViewByAge
        fields = ('post_id', 'age', 'count')


class PostViewByCountrySerializer(ModelSerializer):
    class Meta:
        model = PostViewByCountry
        fields = ('post_id', 'country', 'count')


class PostViewSerializer(ModelSerializer):
    class Meta:
        model = PostView
        fields = '__all__'


class PostViewByUserSerializer(ModelSerializer):
    class Meta:
        model = PostViewByUser
        fields = '__all__'
