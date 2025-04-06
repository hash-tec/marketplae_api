from django.db import models
from access.models import Customer
from django.conf import settings

# Create your models here.
class Coupon(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    coupon_name = models.CharField(max_length = 150)
    code = models.CharField(max_length=7, unique=True)
    identifier =  models.CharField(max_length=50)
    percentage_off = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
    