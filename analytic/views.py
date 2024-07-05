import requests

from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .models import (
    PostView, UserVisit,
)
from .serializers import (
    PostViewSerializer, UserVisitSerializer,
)


class PostViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    def increment_post_view(self, request, *args, **kwargs):
        post_id = request.data.get('post_id')

        if post_id is None:
            return Response("post_id is required", status=status.HTTP_400_BAD_REQUEST)

        post_view = PostView.objects.filter(post_id=post_id).first()

        if post_view is not None:
            post_view.view_count += 1
            post_view.save()

            return Response("Post view successfully added", status=status.HTTP_201_CREATED)

        post_view = PostView.objects.create(post_id=post_id)
        post_view.view_count += 1
        post_view.save()

        return Response("Post view successfully added", status=status.HTTP_201_CREATED)

    def analytics_post_view(self, request, *args, **kwargs):
        post_id = request.data.get('post_id')

        if post_id is None:
            return Response("post_id is required", status=status.HTTP_400_BAD_REQUEST)

        post_view = PostView.objects.filter(post_id=post_id).first()

        if post_view is None:
            return Response("post_id is not found", status=status.HTTP_404_NOT_FOUND)

        serializer = PostViewSerializer(post_view)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    def increment_user_visit(self, request, *args, **kwargs):
        user_id = request.user.id

        if user_id is None:
            return Response("user_id is required", status=status.HTTP_400_BAD_REQUEST)

        post_id = request.data.get("post_id")

        if post_id is None:
            return Response("post_id is required", status=status.HTTP_400_BAD_REQUEST)

        user_visit = UserVisit.objects.filter(user_id=user_id, post_id=post_id).first()

        if user_visit is not None:
            user_visit.view_count += 1
            user_visit.save()

            return Response("User visited successfully", status=status.HTTP_200_OK)

        user_visit = UserVisit.objects.create(user_id=user_id, post_id=post_id)
        user_visit.view_count += 1
        user_visit.save()

        return Response("User visited successfully", status=status.HTTP_201_CREATED)

    def analytics_user_visit(self, request, *args, **kwargs):
        user_id = request.user.id

        if user_id is None:
            return Response("user_id is required", status=status.HTTP_400_BAD_REQUEST)

        post_id = request.data.get("post_id")

        if post_id is None:
            return Response("post_id is required", status=status.HTTP_400_BAD_REQUEST)

        user_visit = UserVisit.objects.filter(user_id=user_id, post_id=post_id).first()

        if user_visit is None:
            return Response("User visited is not found", status=status.HTTP_404_NOT_FOUND)

        serializer = UserVisitSerializer(user_visit)

        return Response(serializer.data, status=status.HTTP_200_OK)
