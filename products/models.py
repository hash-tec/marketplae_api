from django.db import models
from access.models import Customer
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey( Customer, on_delete=models.CASCADE, verbose_name=_("Seller"))
    product_name = models.CharField(_("Product Name"), max_length=200)
    brand = models.CharField(_("Brand"), max_length=50, blank=False)
    description = models.TextField(_("Description"), blank=False)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2, blank=False )
    discount_percentage= models.DecimalField(_("Discount Percentage"), max_digits=10, decimal_places=0, null=True, blank=True)
    image = models.FileField(_("Image"), upload_to="items_images", null=True)
    slug = models.SlugField(default="", null=True)
    date_created = models.DateField(auto_now_add=True)

    def discounted_price(self):
        calc_discount= float(self.price - (round(self.discount_percentage / 100) * self.price, 2))

    def str(self):
        return self.product_name