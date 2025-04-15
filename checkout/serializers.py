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


    # image =  serializers.SerializerMethodField(read_only =True )
    class Meta:
        model = CartItem
        fields = ["id", "product_name", "brand", "price", "discount_percentage","quantity","total_price",  ]

    
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

# class ProfileSerializer(serializers.ModelSerializer):


#     class Meta:
#         model = Cart
# class ShippingAddressSerializer(serializers.ModelSerializer):

    

    
    