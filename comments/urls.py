from django.urls import path
from .views import *

urlpatterns = [
    path('comments/', CommentListApiView.as_view(), name='comment'),
    path('comment-create/', CommentCreateApiView.as_view(), name='comment-create'),
    path('comment/<str:pk>/', CommentDetailDestroyApiView.as_view(), name='comment-detail'),
    path('comment-like/<str:pk>/', CommentLikeApiView.as_view(), name='comment-like'),
    path('repeat-comments/', RepeatCommentListApiView.as_view(), name='repeat-comments'),
    path('repeat-comment-create/', RepeatCommentCreateApiView.as_view(), name='create-repeat-comment'),
    path('repeat-comment/<str:pk>/', RepeatCommentDetailDestroyApiView.as_view(), name='repeat-comment-detail'),
    path('top-comment/', TopCommentsAPIView.as_view(), name='top-comments')
]
