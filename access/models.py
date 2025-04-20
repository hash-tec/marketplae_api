from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .manager import UserManager

# Create your models here.


class Customer(AbstractUser):
    username = None
    email = models.EmailField(_("Email Address"), unique=True)
    bio = models.TextField(_("Bio"), max_length=250, blank = True)
    birthday=models.DateField(_("Birthday"), blank= True, null=True)
    pfp = models.FileField(upload_to="",null=True, blank=True )
    gender_choice = (('M', 'Male'),
                      ('F', 'Female'),)
    gender = models.CharField(_("Gender"), max_length=1, choices=gender_choice)
    phone_number = models.CharField(_("Phone Number"), max_length=15, unique=True, blank=True, null= True )
    date_joined = models.DateField(_("Date Joined"), auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def str(self):
        return self.email
    


class Address(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    label = models.CharField(max_length = 100)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def full_name(self):
        return self.customer.get_full_name()
    
    def address(self):
        return self.street_address, self.city, self.state, self.country
    class Meta:
        verbose_name_plural = "Addresses"
