from django.db import models

# Create your models here.
class Coupon(models.Model):
    coupon_name = models.CharField(max_length = 150)
    percentage_off = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)