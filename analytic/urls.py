from django.urls import path
from .views import (
    PostViewSet, UserViewSet,
)

urlpatterns = [
    path('increment-post-view/', PostViewSet.as_view({'post': 'increment_post_view'})),
    path('list-post-view/', PostViewSet.as_view({'post': 'analytics_post_view'})),

    path('increment-user-visit/', UserViewSet.as_view({'post': 'increment_user_visit'})),
    path('list-user-visit/', UserViewSet.as_view({'post': 'analytics_user_visit'})),
]
