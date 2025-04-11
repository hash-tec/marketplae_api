from django.db import models
from django.conf import settings
from access.models import Customer
from django.utils.translation import gettext_lazy as _
from products.models import Product

# Create your models here.

class Cart(models.Model):
        user = models.OneToOneField(Customer, on_delete=models.CASCADE, null=True)

        def __str__(self):
             return f"{self.user}"
class CartItem(models.Model):
    owner = models.ForeignKey( Cart, on_delete=models.CASCADE, verbose_name=_("Seller"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(_("Quantity"), default=1)

    def __str__(self):
        return f"{self.product.product_name} {self.quantity}"
    


