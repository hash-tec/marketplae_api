from django.urls import path
from .views import ProductListingApiView, ProductListDetailApiView, CategoryApiView



urlpatterns = [
    path('',ProductListDetailApiView.as_view(), name = "all" ),
    path('category/<str:category>/', CategoryApiView.as_view(), name = "name"),
    path('<int:pk>/', ProductListDetailApiView.as_view()),
    path('listing/',ProductListingApiView.as_view(), name = "listing" ),
    
]
