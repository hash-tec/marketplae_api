from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializers
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
        serializer = ProductSerializers(data = request.data, 
                                         context = {"request":request}) 
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response({"message":f"Not valid {seller}", 'data': serializer.error_messages})
       
        

class ProductListDetailApiView(APIView):
    def get(self, request, pk = None):
        if pk:
            instance = Product.objects.get(id = pk)
            serializer = ProductSerializers(instance)
            return Response(serializer.data)
        else:
            instance = Product.objects.all()
            serializer = ProductSerializers(instance, many = True)
            return Response(serializer.data)
 
class CategoryApiView(APIView):
    pass