from django.urls import path
from .views import ProductListingApiView, ProductListDetailApiView



urlpatterns = [
    path('',ProductListDetailApiView.as_view(), name = "all" ),
    path('<int:pk>/', ProductListDetailApiView.as_view()),
    path('listing/',ProductListingApiView.as_view(), name = "listing" ),
    
]
