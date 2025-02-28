from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.

class UserModel(AbstractUser):
    username = None
    email = models.EmailField(_("Email Address"), unique=True)
    bio = models.TextField(_("Bio"), max_length=250, blank = True)
    birthday=models.DateField(_("Birthday"))
    pfp = models.FileField(upload_to="",null=True, blank=True )
    gender_choice = (('M', 'Male'),
                      ('F', 'Female'),)
    gender = models.CharField(_("Gender"), max_length=1, choices=gender_choice)
    phone_number = models.CharField(_("Phone Number"), max_length=15, unique=True)
    address = models.CharField(_("Address"), max_length=250, null=True, blank = True)
    date_joined = models.DateField(_("Date Joined"), default= timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def str(self):
        return self.email