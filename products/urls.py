from django.urls import path
from .views import ProductListingApiView, ProductListDetailApiView, CategoryApiView, ProductDeleteUpdateApiView



urlpatterns = [
    path('',ProductListDetailApiView.as_view()),
    path('listing/',ProductListingApiView.as_view(), name = "listing" ),
    path('<int:pk>/', ProductListDetailApiView.as_view(), name = "detail"),
    path('update/<int:pk>/', ProductDeleteUpdateApiView.as_view(), name = "update"),
    path('delete/<int:pk>/', ProductDeleteUpdateApiView.as_view(), name = "delete"),
    path('category/<str:category>/', CategoryApiView.as_view(), name = "name"),
    
]

