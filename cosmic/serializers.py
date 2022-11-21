from .models import Phone, Coupon
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('phone',)


class CouponSerializer(serializers.ModelSerializer):
    cupon_img = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = Coupon
        fields = ('cupon_img', 'active', 'phone')

    def create(self, validated_data):
        cupon_img = validated_data.pop('cupon_img')
        active = validated_data.pop('active')
        phone = validated_data.pop('phone')
        return Coupon.objects.create(cupon_img=cupon_img, active=active,
                                     phone=phone)
