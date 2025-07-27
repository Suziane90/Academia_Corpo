# users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, user_info

router = DefaultRouter()
router.register(r'usuarios', CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
     path('me/', user_info),
]
