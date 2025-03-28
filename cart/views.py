from django.shortcuts import render
from .models import Cart, CartItem
from products.models import Product
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from .serializers import CartSerializer, AllCartSerializer
from products.serializers import ProductSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# from common.permissions
# Create your views here.


''' AllCartApiView get cart which belongs to the user 
    - 'cart' variable filter out instance that belongs to the current logged in user from the cart items 
    - conditional block is placed to handle error if the user does not have any item in the cart'''
class AllCartApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = Cart.objects.get(user = request.user)
        cart = CartItem.objects.filter(owner = user)
        if cart.exists():
            serializer = AllCartSerializer(cart, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message":"Your cart is empty"}, status=status.HTTP_204_NO_CONTENT)

'''CartApiView adds product to the user cart'''
class CartApiView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request,  *args, **kwargs):
        '''
        product_id extract the dynamic value from the url
        cart_owner get if the logged in user exist in the Cart model and create for a new user
        product uses product_id to fetch the product which is being added to the cart
        try block:
            fetches the product where the product and owner field are the same with the product and cart_owner variable 
            if conditions are meant, the quantity of the product increases rather than creating a new instance of same product
        except block:
            if the product has not been added it create new instance for the product in the cartItem model
        '''
        product_id  = kwargs.get("pk")
        cart_owner, created = Cart.objects.get_or_create(user= request.user)
        product = Product.objects.get(id = product_id)
        try:
            cart = CartItem.objects.get(owner = cart_owner, product = product )
            if cart:
                cart.quantity +=1
                cart.save()
        except CartItem.DoesNotExist:
            cart = CartItem.objects.create(owner = cart_owner, product = product)
            return Response({"message":"Cart is empty"})
        serializer = CartSerializer(cart, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "Invalid"}, status = status.HTTP_400_BAD_REQUEST)
    
'''AddItemApiView functions with the frontend button to add the item from the from the cart page '''
class AddItemApiView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request,  *args, **kwargs):
        cart_id = kwargs.get("pk")
        cart = CartItem.objects.get(id = cart_id )
        cart.quantity +=1
        cart.save()
        return Response(reverse('cart', request=request))

'''RemoveItemApiView functions with the frontend button to reduce the item from the from the cart page '''
class RemoveItemApiView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request,  *args, **kwargs):
        cart_id = kwargs.get("pk")
        cart = CartItem.objects.get( id = cart_id )
        cart.save()
        if cart.quantity < 1:
            cart.delete() 
        return Response(reverse('cart', request=request))
