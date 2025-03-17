from django.shortcuts import render
from .models import Cart, CartItem
from rest_framework.views import APIView
from .serializers import CartSerializer
from rest_framework.response import Response
# from common.permissions
# Create your views here.

class CartApiView(APIView):
    def post(self, request):
        print (request.data)
        
        instance= CartItem.objects.all()
        serializer = CartSerializer(instance, data = request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.validated_data)
        return Response(serializer.data)
    
    def get(self, request):
        instance= CartItem.objects.all()
        serializer = CartSerializer(instance, many = True)
        return Response(serializer.data)
    
        # item = CartItem.objects.create(product_name = )