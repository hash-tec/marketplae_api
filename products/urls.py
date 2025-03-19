from django.urls import path
from . import views



urlpatterns = [
    path('',views.ProductListDetailApiView.as_view()),
    path('listing/',views.ProductListingApiView.as_view(), name = "listing" ),
    path('<int:pk>/', views.ProductListDetailApiView.as_view(), name = "detail"),
    path('update/<int:pk>/', views.ProductDeleteUpdateApiView.as_view(), name = "update"),
    path('delete/<int:pk>/', views.ProductDeleteUpdateApiView.as_view(), name = "delete"),
    path('category/<str:category>/', views.CategoryApiView.as_view(), name = "name"),
    
]

