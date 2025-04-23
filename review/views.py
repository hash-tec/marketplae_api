from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ReviewSerializers, AllReviewsSerializers
from products.models import Product
from .models import Review
from rest_framework.response import Response
from common.permissions import ReviewPermission
# Create your views here.

class ReviewsApiView(APIView):
    permission_classes = [ReviewPermission]
    def post(self, request, **kwargs):
        data = request.data
        product = Product.objects.get (id = kwargs.get('pk'))
        data['reviewer'] = request.user.get_full_name()
        serializer = ReviewSerializers(data= data, context={"request":request})
        if serializer.is_valid():
            serializer.save(product = product)
            return Response("Success")
        return Response(serializer.errors)
    def get(self, request, pk = None):
        if pk is None:
            p_id = Product.objects.get (id = pk)
            reviews = Review.objects.filter(product_id = p_id )
            serializer = AllReviewsSerializers(reviews, many = True)
            return Response (serializer.data)
        else:
            
            reviews = Review.objects.get(id = pk )
            serializer = AllReviewsSerializers(reviews)
            return Response (serializer.data)


