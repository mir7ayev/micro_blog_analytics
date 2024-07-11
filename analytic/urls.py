from django.urls import path
from .views import (
    AnalyticsViewSet,
)

urlpatterns = [

    path('increment-post-view/', AnalyticsViewSet.as_view({'post': 'increment_post_view'})),
    path('increment-view-by-user/', AnalyticsViewSet.as_view({'post': 'increment_view_by_user'})),
    path('increment-view-by-gender/', AnalyticsViewSet.as_view({'post': 'increment_view_by_gender'})),
    path('increment-view-by-age/', AnalyticsViewSet.as_view({'post': 'increment_view_by_age'})),
    path('increment-view-by-country/', AnalyticsViewSet.as_view({'post': 'increment_view_by_country'})),

    path('analytics-post-view/', AnalyticsViewSet.as_view({'get': 'analytics_post_view'})),
    path('analytics-view-by-user/', AnalyticsViewSet.as_view({'get': 'analytics_view_by_user'})),
    path('analytics-view-by-gender/', AnalyticsViewSet.as_view({'get': 'analytics_view_by_gender'})),
    path('analytics-view-by-age/', AnalyticsViewSet.as_view({'get': 'analytics_view_by_age'})),
    path('analytics-view-by-country/', AnalyticsViewSet.as_view({'get': 'analytics_view_by_country'})),

]
