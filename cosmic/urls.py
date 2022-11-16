# from django.conf.urls impor
from django.urls import path, include
from django.urls import re_path
from cosmic import views
from rest_framework import routers


urlpatterns = [
    path('phones/', views.getData),
    path('phone_add/', views.addPhone),
]