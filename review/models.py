from django.db import models
from access.models import Customer
from products.models import Product
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Review(models.Model):
    # product_id = models.IntegerField()
    reviewer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(default = 0)
