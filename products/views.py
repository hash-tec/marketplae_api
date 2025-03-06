from django.shortcuts import render
from .models import Products
from .serializers import ProductsSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


# Create your views here.
class ProductListingApiView(APIView):
    def post(self, request):
        serializer = ProductsSerializers(data = request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)