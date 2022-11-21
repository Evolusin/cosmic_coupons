# from django.conf.urls impor
from django.urls import path, include
from django.urls import re_path
from cosmic import views
from rest_framework import routers


urlpatterns = [
    path('api_phones/', views.getData),
    path('api_phone_add/', views.addPhone),
    path('api_coupon_add/', views.addCoupon),
    path('coupons', views.coupons, name="coupons")
]