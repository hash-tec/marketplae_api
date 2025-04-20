from django.shortcuts import render
from access.models import Customer, Address
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CheckoutSerializer
from cart.models import Cart, CartItem
from access.serializers import AddAddressSerializer
from django.db.models import Sum, F
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

# Create your views here.
class CheckoutApiView(APIView):
    def get(self, request):
        try:
            user = Cart.objects.get(user = request.user)
        except ObjectDoesNotExist:
            return Response({"user_cart_error":"User does not have available cart"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                user_cart = CartItem.objects.filter(owner = user)
            except ObjectDoesNotExist:
                return Response({"cart_error":"No available cart"}, status=status.HTTP_400_BAD_REQUEST)
            else:
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

class ShippingAddress(APIView):
    def get(self, request):
        user = request.user
        phone_no = request.user.phone_number
        try:
            user_address = Address.objects.filter(customer = user)
        except:
            return Response({"user_cart_error":"User does not have available cart"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = AddAddressSerializer(user_address, many= True)
            return Response({"addresses":serializer.data, "number": phone_no})
    def post(self, request):
        pass

class OrderApiView(APIView):
    pass
