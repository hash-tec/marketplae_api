from django.shortcuts import render
from .models import Cart, CartItem
from products.models import Product
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from .serializers import CartSerializer, AllCartSerializer
from products.serializers import ProductSerializers
from rest_framework.response import Response
# from common.permissions
# Create your views here.

class AllCartApiView(APIView):
    def get(self, request):
        user = Cart.objects.get(user = request.user)
        cart = CartItem.objects.filter(owner = user)
        serializer = AllCartSerializer(cart, many = True)
        return Response(serializer.data)

class CartApiView(APIView):
    def get(self, request,  *args, **kwargs):
        ident = kwargs.get("pk")
        owner, created = Cart.objects.get_or_create(user= request.user)
        product= Product.objects.get(id = ident)
        try:
            cart = CartItem.objects.get(owner = owner, product = product )
            if cart:
                cart.quantity +=1
                cart.save()
        except CartItem.DoesNotExist:
            cart = CartItem.objects.create(owner = owner, product = product)
            return Response({"message":"Cart id empty"})

        print(cart.product.product_name, cart.quantity)
        serializer = CartSerializer(cart, request.data, context = {"request":request})
        if serializer.is_valid():
            print("saved")
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response({"message": "Invalid"})
    

class AddItemApiView(APIView):
    def get(self, request,  *args, **kwargs):
        ident = kwargs.get("pk")
        owner = Cart.objects.get(user= request.user)
        cart = CartItem.objects.get( id = ident )
        cart.quantity +=1
        cart.save()
        return Response(reverse('allcart', request=request))
class RemoveItemApiView(APIView):
    def get(self, request,  *args, **kwargs):
        ident = kwargs.get("pk")
        owner = Cart.objects.get(user= request.user)
        cart = CartItem.objects.get( id = ident )
        cart.quantity -=1
        cart.save()
        return Response(reverse('allcart', request=request))
