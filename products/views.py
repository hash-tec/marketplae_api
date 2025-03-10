from django.shortcuts import render
from .models import Products
from .serializers import ProductsSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


# Create your views here.
class ProductListingApiView(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        seller = self.request.user.email
        print(seller)
        serializer = ProductsSerializers(data = request.data, 
                                         context = {"request":request}) 
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response({"message":f"Not valid {seller}", 'data': serializer.error_messages})
       
        

class ProductsApiView(APIView):
    def get(self, request):
        instance = Products.objects.all()
        serializer = ProductsSerializers(instance, many = True)
        return Response(serializer.data)