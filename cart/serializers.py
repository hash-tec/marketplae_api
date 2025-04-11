from rest_framework import serializers
from .models import CartItem, Cart
from decimal import Decimal
from django.db.models import Sum, F
class CartSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField(read_only =True )
    product_name = serializers.SerializerMethodField(read_only =True )
    brand =  serializers.SerializerMethodField(read_only =True )
    description =  serializers.SerializerMethodField(read_only =True )
    price =  serializers.SerializerMethodField(read_only =True )
    discount_percentage= serializers.SerializerMethodField(read_only =True )
    # image =  serializers.SerializerMethodField(read_only =True )
    date_created =  serializers.SerializerMethodField(read_only =True )
    class Meta:
        model = CartItem
        fields = ["owner", "product_name", "brand", "description", "price", "discount_percentage","quantity", "date_created"]

    def get_owner(self, obj):
        return obj.owner.user.email
    
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
    # def get_image(self, obj):
    #     return obj.product.image
    def get_date_created(self, obj):
        return obj.product.date_created

    
class AllCartSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField(read_only =True )
    product_name = serializers.SerializerMethodField(read_only =True )
    brand =  serializers.SerializerMethodField(read_only =True )
    description =  serializers.SerializerMethodField(read_only =True )
    price =  serializers.SerializerMethodField(read_only =True )
    discount_percentage= serializers.SerializerMethodField(read_only =True )
    total_price = serializers.SerializerMethodField(read_only = True)
    cart_amount = serializers.SerializerMethodField(read_only = True)
    # image =  serializers.SerializerMethodField(read_only =True )
    date_created =  serializers.SerializerMethodField(read_only =True )
    class Meta:
        model = CartItem
        fields = ["id", "seller", "product_name", "brand", "description", "price", "discount_percentage","quantity","total_price", "cart_amount", "date_created"]

    def get_seller(self, obj):
        return obj.product.seller.email
    
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
        total_amount = obj.product.price * obj.quantity
        return total_amount
    def get_cart_amount(self):
        user = self.context["request"].user
        user_cart = Cart.objects.get(user = user)
        cart = CartItem.objects.filter(owner = user_cart).aggregate(cart_amount = Sum(F('product__price') * F('quantity')))['cart_amount']
        return cart
    
    # def get_image(self, obj):
    #     return obj.product.image
    def get_date_created(self, obj):
        return obj.product.date_created

    