from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ReviewSerializers
from products.models import Product
from rest_framework.response import Response
# Create your views here.

class ReviewsApiView(APIView):
    def post(self, request):
        user = request.user.full_name
        print(user)
        product = Product.objects.get (id = request.data.get('product_id'))
        serializer = ReviewSerializers(data= request.data)
        if serializer.is_valid():
            serializer['reviewer'] = user
            serializer['product'] = product
            return Response("Sucess")
        return Response("valid")


