from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Cart(models.Model):
        user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

        def __str__(self):
             return f"{self.user}"
class CartItem(models.Model):
    seller = models.ForeignKey( Cart, on_delete=models.CASCADE, verbose_name=_("Seller"))
    product_name = models.CharField(_("Product Name"), max_length=200)
    brand = models.CharField(_("Brand"), max_length=50, blank=False)
    description = models.TextField(_("Description"), blank=False)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2, blank=False )
    category =  models.CharField(_("Category"), max_length=10, null = True )
    image = models.FileField(_("Image"), upload_to="items_images", null=True)


    def __str__(self):
        return f"{self.item_name} {self.quantity}"