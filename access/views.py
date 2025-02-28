from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from .models import UserModel
from .serializers import RegisterUserSerializer

class RegisterUserApiView(APIView):
    def post(self, request, *args, **kwargs):
        Serializer = RegisterUserSerializer(data = request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status= status.HTTP_201_CREATED)
        return Response(Serializer.errors, status = status.HTTP_400_BAD_REQUEST)

