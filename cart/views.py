from django.shortcuts import render
from .models import Cart, CartItem
from products.models import Product
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from .serializers import CartSerializer, AllCartSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# from common.permissions
# Create your views here.

'''
    CartViewset handles all the request going through the cart endpoint
    functions:
        get_permissions: Handles the the action which can be perform according to the request method
        list: Get all the items that has been added to the logged in user cart
        post: Handles the how ta product listing is added to the user quantity
            - cart_owner:checks if the user has previously added an item to cart, regardless if the cart is empty at the time,
              the Cart model will still have the instance of the user
            - try block: checks if the the item has been previously added to the cart, if True it adds to the quantity of the product
            - except block: if the item is yet to be added t the cart, adds the item to the cart

'''
class CartViewset(ViewSet):
    def get_permissions(self):
        if self.action == 'list':
            return []
        elif self.action == 'partial_update':
            return [IsAuthenticated()]
        return super().get_permissions()
    def list(self, request):
        user = Cart.objects.get(user = request.user)
        cart = CartItem.objects.filter(owner = user)
        if cart.exists():
            serializer = AllCartSerializer(cart, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message":"Your cart is empty"}, status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request,  *args, **kwargs):

        # product_id extract the dynamic value from the url with the identifier PK
        product_id  = kwargs.get("pk")
        # checks for the logged in user if it has an instance in the cart, if False, it create new instance for the user 
        cart_owner, created = Cart.objects.get_or_create(user= request.user)
        product = Product.objects.get(id = product_id)
        try:
            cart = CartItem.objects.get(owner = cart_owner, product = product )
            serializer = CartSerializer(cart, request.data)
            cart.quantity +=1
            cart.save()
        except CartItem.DoesNotExist:
            cart = CartItem.objects.create(owner = cart_owner, product = product)
            serializer = CartSerializer(cart, request.data)
            return Response(serializer.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "Invalid"}, status = status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        action = request.data.get("action", "increase")
        if action == "increase":
            cart_id = kwargs.get("pk")
            cart = CartItem.objects.get(id = cart_id )
            cart.quantity +=1
            cart.save()
            return Response(reverse('cart', request=request), status=status.HTTP_200_OK)
        elif action == "decrease":
            cart_id = kwargs.get("pk")
            cart = CartItem.objects.get( id = cart_id )
            print(cart.quantity)
            cart.quantity -= 1
            print("after", cart.quantity)
            cart.save()
            if cart.quantity < 1:
                cart.delete() 
            return Response(reverse('cart', request=request), status=status.HTTP_200_OK)
        else:
            return Response (status=status.HTTP_400_BAD_REQUEST)