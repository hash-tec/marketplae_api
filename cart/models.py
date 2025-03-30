from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from products.models import Product

# Create your models here.

class Cart(models.Model):
        user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

        def __str__(self):
             return f"{self.user}"
class CartItem(models.Model):
    owner = models.ForeignKey( Cart, on_delete=models.CASCADE, verbose_name=_("Seller"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(_("Quantity"), null=True, default=1)

    def __str__(self):
        return f"{self.product.product_name} {self.quantity}"
    
class Coupon(models.Model):
    coupon_name = models.CharField(max_length = 150)
    percentage_off = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

