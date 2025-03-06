from django.urls import path
from .views import ProductListingApiView



urlpatterns = [
    path('listing/',ProductListingApiView.as_view(), name = "listing" ),
]
