from django.urls import path
from . import views
urlpatterns = [
    path('cart/', views.AllCartApiView.as_view(), name="allcart"),
    path('add-cart/<int:pk>/',views.CartApiView.as_view()),
    path('item-addition/<int:pk>/', views.AddItemApiView.as_view()),
    path('item-sub/<int:pk>/', views.RemoveItemApiView.as_view()),
]
