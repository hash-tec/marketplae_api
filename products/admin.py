from django.contrib import admin
from .models import Product

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ["product_name"]
    prepopulated_fields = {"slug":("product_name", )}
    
admin.site.register(Product, ProductsAdmin)