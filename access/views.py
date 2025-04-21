from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from common.permissions import AuthorEditOnly


# Create your views here.
from .models import Address
from .serializers import RegisterUserSerializer, AddressSerializer

class RegisterUserApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data = request.data)
        if serializer.is_valid():
             serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AddressApiView(APIView):
    permission_classes = [AuthorEditOnly]
    def post(self, request):
        user = request.user
        serializer = AddressSerializer(data = request.data, context = {"request":request})
        if serializer.is_valid():
            address_entries = Address.objects.filter(customer = user).count()
            if address_entries == 3:
                return Response ("You can only have three shipping address", status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    def get(self, request, pk = None):
        if pk is None:
            user = request.user
            instance = Address.objects.filter(customer = user)
            serializer = AddressSerializer(instance, many = True)
            return Response(serializer.data)
        else:
            user = request.user
            instance = Address.objects.get(id = pk)
            serializer = AddressSerializer(instance)
            return Response(serializer.data)
        
    def delete(self, request, pk):
        instance = Address.objects.get(id = pk)
        instance.delete()
        return Response("Address has been deleted")
       
    
