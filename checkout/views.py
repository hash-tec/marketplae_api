from django.shortcuts import render
from access.models import Customer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CheckoutSerializer
from cart.models import Cart, CartItem
# Create your views here.
class CheckoutApiView(APIView):
    def get(self, request):
        user = Cart.objects.get(user = request.user)
        user_cart = CartItem.objects.filter(owner = user)
        user_email = request.user.email
        user_address = request.user.address
        serializer = CheckoutSerializer(user_cart, many = True, context = {"request":request})
        return Response(serializer.data)

        # print(user, user_email)
        # cart = CartItem.objects.filter(owner = user)
        # print(cart)
        # return Response("hi")
