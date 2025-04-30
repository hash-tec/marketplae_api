from django.urls import path
from . import views



urlpatterns = [
    path('', views.ProductApiView.as_view(), name = 'products'),
    path('<int:pk>/', views.ProductApiView.as_view(), name = 'products'),
    path('listing/',views.ProductListingApiView.as_view(), name = "listing" ),
    path('category/<str:category>/', views.CategoryApiView.as_view(), name = "name"),
]

