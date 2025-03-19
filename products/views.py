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
class ProductListDetailApiView(APIView):
    permission_classes = [UserPermission]
    def get_queryset(self):
        return Product.objects.all()
    
    def get(self, request, pk = None):
        if pk:
            instance = Product.objects.get(id = pk)
            serializer = ProductSerializers(instance, context = {"request":request})
            return Response(serializer.data)
        else:
            instance = Product.objects.all()
            serializer = ProductSerializers(instance, many = True,  context = {"request":request})
            return Response(serializer.data)
 
class ProductDeleteUpdateApiView(APIView):
    def put(self, request, pk):
        instance = Product.objects.get(pk = pk)
        print(request.data)
    
        serializer = ProductSerializers(instance, data = request.data, partial = True, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            print("Valid",serializer.error_messages)
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.error_messages)
    # def patch(self, request, pk):
    #     instance = Product.objects.get(pk = pk)
    #     serializer = ProductSerializers(instance, data = request.data, partial = True, context = {'request': request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         print("Valid",serializer.validated_data)

    #         return Response(serializer.data, status= status.HTTP_200_OK)
    #     else:
    #         print(serializer.errors)
    #         return Response(serializer.validated_data)

    def delete(self, request, pk):
        instance = Product.objects.get(pk = pk)
        if instance:
            instance.delete()
            return Response({"message": "Item delist "}, status = status.HTTP_200_OK)
        
class CategoryApiView(APIView):
    def get(self, request, *args, **kwargs):
        section = kwargs.get("category")
        instance = Product.objects.filter(category = section)
        if instance.exists():
            serializer = ProductSerializers(instance, many = True, context = {'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(({'errors':"This is an invalid category"}), status=status.HTTP_404_NOT_FOUND)