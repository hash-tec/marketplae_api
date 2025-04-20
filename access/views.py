from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


# Create your views here.
from .models import Address
from .serializers import RegisterUserSerializer, AddAddressSerializer

class RegisterUserApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data = request.data)
        if serializer.is_valid():
             serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AddAddressApiView(APIView):
    def post(self, request):
        user = request.user
        serializer = AddAddressSerializer(data = request.data, context = {"request":request})
        if serializer.is_valid():
            address_entries = Address.objects.filter(customer = user).count()
            if address_entries == 3:
                return Response ("You can only have three shipping address", status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
       
    
