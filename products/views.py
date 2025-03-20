from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from common.permissions import UserPermission
from rest_framework import status, viewsets


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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response({"message":f"Not valid {seller}", 'data': serializer.error_messages})
       
        
class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        instance = Product.objects.all()
        serializer = ProductSerializers(instance, many = True, context = {"request":request})
        return Response(serializer.data)
    def retrieve(self, request, pk):
        instance = Product.objects.get(id = pk)
        serializer = ProductSerializers(instance, context = {"request":request})
        return Response(serializer.data)
    def update(self, request, pk):
        instance = Product.objects.get(id = pk)
        serializer = ProductSerializers(instance,request.data, context = {"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def partial_update(self, request, pk):
        instance = Product.objects.get(id = pk)
        serializer = ProductSerializers(instance,request.data,partial = True, context = {"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"message": "deleted"})
    def destroy(self, request, pk):
        instance = Product.objects.get(id = pk)
        instance.delete()
        return Response({"message": "deleted"})

class CategoryApiView(APIView):
    def get(self, request, *args, **kwargs):
        section = kwargs.get("category")
        instance = Product.objects.filter(category = section)
        if instance.exists():
            serializer = ProductSerializers(instance, many = True, context = {'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(({'errors':"This is an invalid category"}), status=status.HTTP_404_NOT_FOUND)