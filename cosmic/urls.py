# from django.conf.urls impor
from django.urls import path, include
from django.urls import re_path
from .views import (
    PhoneViewSet,
)
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'phones', PhoneViewSet, basename='phones')

urlpatterns = [
    re_path(r'^api/', include(router.urls)),
]