from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', PostListApiView.as_view(), name='posts'),
    path('post/<str:pk>/', PostDetailApiView.as_view(), name='post-detail'),
    path('post-create/', PostCreateApiView.as_view(), name='post-create'),
    path('like/<str:pk>/', PostLikeApiView.as_view(), name='post-like'),
    path('top-posts/', TopPostsAPIView.as_view(), name='top-posts'),
    path('report/', ReportPostAPiView.as_view(), name='report-post'),
]
