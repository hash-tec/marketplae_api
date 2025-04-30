from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from common.permissions import UserPermission, AuthorEditOnly
from rest_framework import status, viewsets
from coupons.serializers import CouponSerializers
from rest_framework.pagination import PageNumberPagination
# Create your views here.

''' ProductListingApiView allows the creation of an item by creating an instance of the Product models'''
class ProductListingApiView(APIView):
    def post(self, request):
        serializer = ProductSerializers(data = request.data, context = {"request":request}) 
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data, "error":serializer.errors},status=status.HTTP_201_CREATED)
        else: 
            return Response({"message": "Error listing your item", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
       
        
''' get_permissions restrict permissions to some views using a customized permission class
    pk passed as an argument in retrieve, update, partial_update is a dynamic value passed from the URL in which pk is the identifier
'''
class ProductApiView(APIView):
    def get(self, request, pk = None):
        if pk is None:
            instance = Product.objects.all()
            serializer = ProductSerializers(instance, many = True, context = {"request":request})
            return Response(serializer.data)
        else:
            instance = Product.objects.get(id = pk)
            serializer = ProductSerializers(instance, context = {"request":request})
            return Response(serializer.data)
        
    def put(self, request, pk):
        instance = Product.objects.get(id = pk)
        serializer = ProductSerializers(instance, request.data, context = {"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def patch(self, request, pk):
            instance = Product.objects.get(id = pk)
            serializer = ProductSerializers(instance,request.data, context = {"request":request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

    def destroy(self, request, pk):
        instance = Product.objects.get(id = pk)
        instance.delete()
        return Response({"message": "deleted"})

'''- 'CategoryApiView' filter out categories according to the choice chosen by the seller in the category field in Product model
   - 'section' variable uses the kwargs function to extract the dynamic value in the URL with 'category' as an identifier 
   - 'section' variable is being used to filter all items in each category 
   - 'choice ' variable loops through all the choices in the category_choice in the product model and extract the first key using 'item[0]'
   - if 'section' variable is not in the choice list meaning no such category in database,
   - if 'section' variable is in choice but the 'instance' variable DoesNotExist, prompt the user to add into the
     category as it is in the database list of choices
'''
class CategoryApiView(APIView):
    def get(self, request, *args, **kwargs):
        section = kwargs.get("category")
        men_categories = ['man_tshirt', 'man_shoes', 'manwork_equipment', 'man_pants', 'man_underwear']
        women_categories = ['dress', 'woman_tshirt', 'woman_pants', 'skirts', 'bags', 'high_heels', 'bikini']
        categories = []
        # The for loop block get the choices keys saved into the database from the product model, and it is appended into the categories list
        for category in Product.category_choice:
            print ("category", category)
            for subcategory in category[1]:
                sub_category = subcategory[0]
                categories.append(sub_category)
        ''' This if and elif block get all the product similar to Men's and Women's product 
        - if the dynamic url is 'men' the  it queries for all the product with the category in the list 'men_categories' 
        - if the dynamic url is 'women' the  it queries for all the product with the category in the list 'women_categories' '''
        if section =='men':
            instance = Product.objects.filter(category__in = men_categories)
            serializer = ProductSerializers(instance, many = True, context = {'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif section =='women':
            instance = Product.objects.filter(category__in = women_categories)
            serializer = ProductSerializers(instance, many = True, context = {'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        '''This if and else block is to filter product according to it category, it queries the category field against the dynamic
          url value
          - If block is to check if the dynamic url value is a valid choice, if not it return a 404 error
          -else block 
            - if block runs the query to get the products belonging to the category
            - else block return a response if the dynamic value is valid in the category choice but no product has been added to the category'''
        if not section in categories:
            return Response({"message": "Invalid category"}, status=status.HTTP_404_NOT_FOUND)
        else:
            instance = Product.objects.filter(category = section)
            if instance.exists():
                serializer = ProductSerializers(instance, many = True, context = {'request':request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(({'message':"Be the first to add into this category"}), status=status.HTTP_404_NOT_FOUND)