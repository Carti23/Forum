from django.urls import path

from .views import SearchApiView

urlpatterns = [
    path('', SearchApiView.as_view(), name='search'),
]