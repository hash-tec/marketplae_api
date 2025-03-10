from django.urls import path
from .views import ProductListingApiView, ProductsApiView



urlpatterns = [
    path('',ProductsApiView.as_view(), name = "all" ),
    path('listing/',ProductListingApiView.as_view(), name = "listing" ),
    
]
