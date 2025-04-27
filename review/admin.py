from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["full_name", "rating"]

admin.site.register(Review, ReviewAdmin)

# Register your models here.
