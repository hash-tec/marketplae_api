from django.shortcuts import render
from .models import Cart, CartItem
from products.models import Product
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from .serializers import CartSerializer, AllCartSerializer
from access.models import Customer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ValidationError

# Create your views here.

'''
    CartApiView handles all the request going through the cart endpoint
    functions:
            get: Get all the items that has been added to the logged in user cart
            post: Handles the how ta product listing is added to the user quantity
            patch: Increase or decrease the quantity of the product based of the action passed, the client is expected to pass Increase or Decrease
            - cart_owner:checks if the user has previously added an item to cart, regardless if the cart is empty at the time,
              the Cart model will still have the instance of the user
            - try block: checks if the the item has been previously added to the cart, if True it adds to the quantity of the product
            - except block: if the item is yet to be added t the cart, adds the item to the cart

'''
class CartApiView(APIView):

    permission_classes = [IsAuthenticated ]
    def get(self, request, *args, **kwargs):
        user, created = Cart.objects.get_or_create(user = request.user)
        cart = CartItem.objects.filter(owner = user)
        if cart.exists():
            serializer = AllCartSerializer(cart, many = True, context = {"request": request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message":"Your cart is empty"}, status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request, pk):
        # checks for the logged in user if it has an instance in the cart, if False, it create new instance for the user 
        cart_owner, created = Cart.objects.get_or_create(user= request.user)
        try:
            product = Product.objects.get(id = pk)
        except:
            raise ValidationError("product id not found")
        else:
            try:
                cart = CartItem.objects.get(owner = cart_owner, product = product )
                serializer = CartSerializer(cart, request.data)
                cart.quantity +=1
                cart.save()

            except CartItem.DoesNotExist:
                cart = CartItem.objects.create(owner = cart_owner, product = product)
                serializer = CartSerializer(cart, request.data)
            else:
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response({"message": "Invalid"}, status = status.HTTP_400_BAD_REQUEST)

    '''
        This patch request is to increase an item quantity in a cart with the + and - button, for it to work, either increase
        or decrease has to be passed into the data being passed for the request.
    
    '''
    def patch(self, request, *args, **kwargs):
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
            cart.quantity -= 1
            cart.save()
            if cart.quantity < 1:
                cart.delete() 
            return Response(reverse('cart', request=request), status=status.HTTP_200_OK)
        else:
            return Response (status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
        cart_id = kwargs.get("pk")
        cart = CartItem.objects.get(id = cart_id )
        cart.delete()
        return Response({"message": "Item Removed"}, status=status.HTTP_200_OK)
    




