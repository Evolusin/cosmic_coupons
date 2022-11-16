from django.db import models

# Create your models here.


class Phone(models.Model):

    def __str__(self):
        return self.phone

    phone = models.CharField(max_length=30)
    username = models.CharField(max_length=50)


class Coupon(models.Model):
    cupon_img = models.FileField(upload_to='cosmic/coupons/')
    active = models.BooleanField(default=True)
    created_date = models.DateField('Coupon creation date', auto_now_add=True)
    use_date = models.DateField(null=True, blank=True)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
