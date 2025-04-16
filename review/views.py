from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ReviewSerializers
from products.models import Product
from rest_framework.response import Response
# Create your views here.

class ReviewsApiView(APIView):
    def post(self, request, **kwargs):
        data = request.data
        product = Product.objects.get (id = kwargs.get('pk'))
        data["reviewer"] = request.user.get_full_name()
        serializer = ReviewSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save(product = product)
            return Response("Success")
        return Response(serializer.errors)


