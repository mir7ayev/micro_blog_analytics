import requests

from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.conf import settings
from .models import (
    PostView, PostViewByUser, PostViewByAge, PostViewByCountry,
    PostViewByGender,
)
from .serializers import (
    PostViewSerializer, PostViewByUserSerializer, PostViewByAgeSerializer,
    PostViewByCountrySerializer, PostViewByGenderSerializer
)


class AnalyticsViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    def get_service_access_token(self):
        response = requests.post(
            url="http://127.0.0.1:",
            data={'secret_key': settings.AUTH_SECRET_KEY}
        )
        if response.status_code != 200:
            raise ValueError("Failed to get service access token")

        return response.json().get('service_access_token')

    def get_user_data(self, user_access_token):
        service_access_token = self.get_service_access_token()
        response = requests.get(
            url="http://127.0.0.1:",
            headers={'Authorization': f'Bearer {service_access_token}'},
            data={'user_access_token': user_access_token}
        )
        if response.status_code != 200:
            raise ValueError("Failed to get user data")

        return response.json()

    def increment_view(self, request, model_class, filter_field, user_field):
        post_id = request.data.get('post_id')
        if post_id is None:
            return Response("post_id is required", status=status.HTTP_404_NOT_FOUND)

        user_access_token = request.data.get('Authorization')
        if user_access_token is None:
            return Response("user_access_token is required", status=status.HTTP_404_NOT_FOUND)

        user_data = self.get_user_data(user_access_token)
        user_field_value = user_data.get(user_field)

        view_obj = model_class.objects.filter(post_id=post_id, **{filter_field: user_field_value}).first()
        if view_obj is None:
            view_obj = model_class.objects.create(post_id=post_id, **{filter_field: user_field_value})

        view_obj.count += 1
        view_obj.save()

        return Response("success", status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        method='post',
        operation_summary="Increment Post View Count",
        operation_description="Increment the view count of a post.",
        responses={status.HTTP_201_CREATED: "success"},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'post_id': openapi.Schema(type=openapi.TYPE_INTEGER),
            },
            required=['post_id']
        ),
        tags=['increment']
    )
    @action(detail=True, methods=['post'])
    def increment_post_view(self, request, *args, **kwargs):
        post_id = request.data.get('post_id')
        if post_id is None:
            return Response("post_id is required", status=status.HTTP_404_NOT_FOUND)

        post_view_obj = PostView.objects.filter(post_id=post_id).first()
        if post_view_obj is None:
            post_view_obj = PostView.objects.create(post_id=post_id)

        post_view_obj.count += 1
        post_view_obj.save()

        return Response("success", status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_description="Increment view count by user",
        operation_summary="Increment View Count by User",
        responses={status.HTTP_201_CREATED: "success"},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user_id': openapi.Schema(type=openapi.TYPE_INTEGER),
                'post_id': openapi.Schema(type=openapi.TYPE_INTEGER)
            },
            required=['user_id', 'post_id']
        ),
        tags=['increment']
    )
    @action(detail=True, methods=['post'])
    def increment_view_by_user(self, request, *args, **kwargs):
        return self.increment_view(request, PostViewByUser, 'user_id', 'id')

    @swagger_auto_schema(
        operation_description="Increment view count by gender",
        operation_summary="Increment View Count by Gender",
        responses={status.HTTP_201_CREATED: "success"},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'gender': openapi.Schema(type=openapi.TYPE_STRING),
                'post_id': openapi.Schema(type=openapi.TYPE_INTEGER)
            },
            required=['gender', 'post_id']
        ),
        tags=['increment']
    )
    @action(detail=True, methods=['post'])
    def increment_view_by_gender(self, request, *args, **kwargs):
        return self.increment_view(request, PostViewByGender, 'gender', 'gender')

    @swagger_auto_schema(
        operation_description="Increment view count by age",
        operation_summary="Increment View Count by Age",
        responses={status.HTTP_201_CREATED: "success"},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'age': openapi.Schema(type=openapi.TYPE_INTEGER),
                'post_id': openapi.Schema(type=openapi.TYPE_INTEGER)
            },
            required=['age', 'post_id']
        ),
        tags=['increment']
    )
    @action(detail=True, methods=['post'])
    def increment_view_by_age(self, request, *args, **kwargs):
        return self.increment_view(request, PostViewByAge, 'age', 'age')

    @swagger_auto_schema(
        operation_description="Increment view count by country",
        operation_summary="Increment View Count by Country",
        responses={status.HTTP_201_CREATED: "success"},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'country': openapi.Schema(type=openapi.TYPE_STRING),
                'post_id': openapi.Schema(type=openapi.TYPE_INTEGER)
            },
            required=['country', 'post_id']
        ),
        tags=['increment']
    )
    @action(detail=True, methods=['post'])
    def increment_view_by_country(self, request, *args, **kwargs):
        return self.increment_view(request, PostViewByCountry, 'country', 'country')

    @swagger_auto_schema(
        operation_description="Retrieve analytics for post views",
        operation_summary="Get Post Views Analytics",
        responses={status.HTTP_200_OK: PostViewSerializer(many=True)},
        tags=['analytics']
    )
    @action(detail=False, methods=['get'])
    def analytics_post_view(self, request, *args, **kwargs):
        analytics = PostView.objects.all().order_by('-count')
        serializer = PostViewSerializer(analytics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Retrieve analytics for post views by user",
        operation_summary="Get Post Views by User Analytics",
        responses={status.HTTP_200_OK: PostViewByUserSerializer(many=True)},
        tags=['analytics']
    )
    @action(detail=False, methods=['get'])
    def analytics_view_by_user(self, request, *args, **kwargs):
        analytics = PostViewByUser.objects.all().order_by('-count')
        serializer = PostViewByUserSerializer(analytics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Retrieve analytics for post views by gender",
        operation_summary="Get Post Views by Gender Analytics",
        responses={status.HTTP_200_OK: PostViewByGenderSerializer(many=True)},
        tags=['analytics']
    )
    @action(detail=False, methods=['get'])
    def analytics_view_by_gender(self, request, *args, **kwargs):
        analytics = PostViewByGender.objects.all().order_by('-count')
        serializer = PostViewByGenderSerializer(analytics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Retrieve analytics for post views by age",
        operation_summary="Get Post Views by Age Analytics",
        responses={status.HTTP_200_OK: PostViewByAgeSerializer(many=True)},
        tags=['analytics']
    )
    @action(detail=False, methods=['get'])
    def analytics_view_by_age(self, request, *args, **kwargs):
        analytics = PostViewByAge.objects.all().order_by('-count')
        serializer = PostViewByAgeSerializer(analytics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Retrieve analytics for post views by country",
        operation_summary="Get Post Views by Country",
        responses={status.HTTP_200_OK: PostViewByCountrySerializer(many=True)},
        tags=['analytics']
    )
    @action(detail=False, methods=['get'])
    def analytics_view_by_country(self, request, *args, **kwargs):
        analytics = PostViewByCountry.objects.all().order_by('-count')
        serializer = PostViewByCountrySerializer(analytics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
