from django.db import models
from access.models import Customer
from products.models import Product
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Review(models.Model):
    reviewer = models.CharField(_("Reviewer"), max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(default = 0)
