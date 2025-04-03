from django.shortcuts import render
from .serializers import CouponSerializers


# Create your views here.


# class Coupon(Apiview):
#     def post(self, request):
#         coupon_serializer= CouponSerializers(request.data, context = {"request":request})
#         if coupon_serializer.is_valid():
#             coupon_serializer.save()
#         return Response({"data":coupon_serializer.data, "errors":coupon_serializer.errors})