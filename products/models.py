from django.db import models
from access.models import Customer
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


# Create your models here.
class Product(models.Model):
    category_choice =(('men', "Men's Wear"), ('women', "Women's Wear"),
                      ('footwears', "Footwears"), ('bags', "Bags"))
    
    seller = models.ForeignKey( Customer, on_delete=models.CASCADE, verbose_name=_("Seller"))
    product_name = models.CharField(_("Product Name"), max_length=200)
    brand = models.CharField(_("Brand"), max_length=50, blank=False)
    description = models.TextField(_("Description"), blank=False)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2, blank=False )
    discount_percentage= models.DecimalField(_("Discount Percentage"), max_digits=10, decimal_places=0, null=True, blank=True)
    category =  models.CharField(_("Category"), choices=category_choice, max_length=10, null = True )
    image = models.FileField(_("Image"), upload_to="items_images", null=True)
    slug = models.SlugField(default="", null=True)
    date_created = models.DateField(auto_now_add=True)

    def get_discounted_price(self):
        if self.discount_percentage:
            discount = (float(self.discount_percentage) / 100) * float(self.price)
            calc_discount = round(float(self.price)- discount, 2)
            return calc_discount
        else:
            return("Discount is NIL")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
            super().save(*args, **kwargs)

    def str(self):
        return self.product_name