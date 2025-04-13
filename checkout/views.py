from django.shortcuts import render
from access.models import Customer, Address
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CheckoutSerializer
from cart.models import Cart, CartItem
from coupons.models import Coupon
from django.db.models import Sum, F
# Create your views here.
class CheckoutApiView(APIView):
    def get(self, request):
        user = Cart.objects.get(user = request.user)
        user_cart = CartItem.objects.filter(owner = user)
        checkout_amount= CartItem.objects.filter(owner = user).aggregate(total_amount = Sum(F('product__price') * F('quantity')))["total_amount"]
        user_address = request.user.address
        if not user_address:
            return Response("You need a valid delivery address")
        serializer = CheckoutSerializer(user_cart, many = True, context = {"request":request})
        return Response({"data":serializer.data, "checkout_amount":checkout_amount , "address": user_address})
    def patch(self, request):
        response_data = request.data.get("code")
        user = Cart.objects.get(user = request.user)
        coupon = coupon.objects.get(code = response_data)

    


        # print(user, user_email)
        # cart = CartItem.objects.filter(owner = user)
        # print(cart)
        # return Response("hi")

class ShippingAddress(APIView):
    def get(self, request):
        user = request.self
        user_address = Address.objects.filter(Customer = user)
        
