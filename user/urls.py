from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('profile/', ProfileListApiView.as_view(), name='profile'),
    path('profile/<str:pk>/', ProfileDetailApiView.as_view(), name='update-profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('post-profile/', PostUserApiView.as_view(), name='profile-post'),
    path('sent-friend-request/<str:pk>/', SentFriendRequestView.as_view(), name='sent-friend-request'),
    path('add-friend/', AddFriendView.as_view(), name='add-friend'),
    path('add-follower/', AddFollowerView.as_view(), name='add-follower'),
    path('remove-friend/', RemoveFriendsApiView.as_view(), name='remove-friend'),
    path('add-block/', AddToBlockApiView.as_view(), name='add-to-block'),
    path('remove-block/', DeleteFromBlockApiView.as_view(), name='remove-to-block'),
]
