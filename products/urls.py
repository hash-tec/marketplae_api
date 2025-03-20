from django.urls import path
from . import views



urlpatterns = [
    path('listing/',views.ProductListingApiView.as_view(), name = "listing" ),
    path('category/<str:category>/', views.CategoryApiView.as_view(), name = "name"),
]

