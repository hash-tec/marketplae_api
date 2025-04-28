from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from common.permissions import UserPermission, AuthorEditOnly
from rest_framework import status, viewsets
from coupons.serializers import CouponSerializers
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
       
        
'''ProductViewSet handles the CRUD operations using viewset and routers'''
class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all() 
    ''' get_permissions restrict permissions to some views using a customized permission class
        pk passed as an argument in retrieve, update, partial_update is a dynamic value passed from the URL in which pk is the identifier
        '''

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return []
        elif self.action in ["update", "partial_update"]:
            return [UserPermission()]
        elif self.action == "destroy":
            return[UserPermission()]
        else:
            return[IsAuthenticated()]
    def list(self, request):
        instance = Product.objects.all()
        serializer = ProductSerializers(instance, many = True, context = {"request":request})
        return Response(serializer.data)
    def retrieve(self, request, pk):
        instance = Product.objects.get(id = pk)
        serializer = ProductSerializers(instance, context = {"request":request})
        return Response(serializer.data)
    def update(self, request, pk):
        instance = Product.objects.get(id = pk)
        serializer = ProductSerializers(instance, request.data, context = {"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def partial_update(self, request, pk):
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
        for category in Product.category_choice:
            print ("category", category)
            for subcategory in category[1]:
                sub_category = subcategory[0]
                categories.append(sub_category)
        
        if section =='men':
            instance = Product.objects.filter(category__in = men_categories)
            serializer = ProductSerializers(instance, many = True, context = {'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif section =='women':
            instance = Product.objects.filter(category__in = women_categories)
            serializer = ProductSerializers(instance, many = True, context = {'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        if not section in categories:
            return Response({"message": "Invalid category"}, status=status.HTTP_404_NOT_FOUND)
        else:
            instance = Product.objects.filter(category = section)
            if instance.exists():
                serializer = ProductSerializers(instance, many = True, context = {'request':request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(({'message':"Be the first to add into this category"}), status=status.HTTP_404_NOT_FOUND)