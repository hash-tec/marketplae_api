from rest_framework import serializers
from cart.models import CartItem, Cart
from decimal import Decimal
from django.db.models import Sum, F

class CheckoutSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField(read_only =True )
    brand =  serializers.SerializerMethodField(read_only =True )
    price =  serializers.SerializerMethodField(read_only =True )
    discount_percentage= serializers.SerializerMethodField(read_only =True )
    total_price = serializers.SerializerMethodField(read_only = True)
    checkout_amount = serializers.SerializerMethodField(read_only = True)
    # image =  serializers.SerializerMethodField(read_only =True )
    class Meta:
        model = CartItem
        fields = ["id", "product_name", "brand", "price", "discount_percentage","quantity","total_price", "checkout_amount"]

    
    def get_product_name(self, obj):
        return obj.product.product_name
    def get_brand(self, obj):
        return obj.product.brand
    def get_description(self, obj):
        return obj.product.description
    def get_price(self, obj):
        return obj.product.price
    def get_discount_percentage(self, obj):
        return obj.product.discount_percentage
    def get_total_price(self, obj):
        if obj.product.discount_percentage:
            discount = obj.product.price *  Decimal(obj.product.discount_percentage / 100)
            amount = obj.product.price - discount
            total_amount = amount * obj.quantity
            return total_amount
    def get_checkout_amount(self, obj):
        user = self.context["request"].user
        user_cart = Cart.objects.get(user = user)
        cart = CartItem.objects.filter(owner = user_cart).aggregate(total_amount = Sum(F('product__price') * F('quantity')))["total_amount"]
        return cart
    
    # def get_image(self, obj):
    #     return obj.product.image
    def get_date_created(self, obj):
        return obj.product.date_created

    
    