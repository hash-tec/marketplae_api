from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ReviewSerializers, AllReviewsSerializers
from products.models import Product
from .models import Review
from rest_framework.response import Response
from rest_framework import status
from common.permissions import ReviewPermission
# Create your views here.

class ReviewsApiView(APIView):
    permission_classes = [ReviewPermission]
    def post(self, request, **kwargs):
        data = request.data
        product = Product.objects.get (id = kwargs.get('pk'))
        serializer = ReviewSerializers(data= data, context={"request":request, "product_id": product })
        if serializer.is_valid():
            serializer.save()
            return Response("Success")
        return Response(serializer.errors)
    
    def get(self, request, pk):
        p_id = Product.objects.get(id = pk)
        try: 
            p_id = Product.objects.get (id = pk)
        except:
            return Response("No Review")
        else:
            reviews = Review.objects.filter(product_id = p_id )
            serializer = AllReviewsSerializers(reviews, many = True)
            return Response (serializer.data)
