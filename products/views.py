from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
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
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, pk = None):
        if pk:
            instance = Product.objects.get(id = pk)
            serializer = ProductSerializers(instance, context = {"request":request})
            return Response(serializer.data)
        else:
            instance = Product.objects.all()
            serializer = ProductSerializers(instance, many = True,  context = {"request":request})
            return Response(serializer.data)
 
class CategoryApiView(APIView):
    def get(self, request, *args, **kwargs):
        section = kwargs.get("category")
        instance = Product.objects.filter(category = section)
        if instance.exists():
            serializer = ProductSerializers(instance, many = True, context = {'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(({'errors':"This is an invalid category"}), status=status.HTTP_404_NOT_FOUND)