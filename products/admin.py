from django.contrib import admin
from .models import Product

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ["product_name", 'seller']
    prepopulated_fields = {"slug":("product_name", )}
    ordering =['-date_created']
    
admin.site.register(Product, ProductsAdmin)