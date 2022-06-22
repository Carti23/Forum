from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user.urls')),
    path('api/', include('post.urls')),
    path('api/v1/base-auth/', include('rest_framework.urls')),
    path('api/', include('comments.urls')),
    path('api/', include('search.urls')),
    path('api/', include('social_auth.urls')),
    path('friendship/', include('friendship.urls'))
]
