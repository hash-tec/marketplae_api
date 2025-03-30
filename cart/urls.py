from django.urls import path
from . import views
urlpatterns = [
    path('cart/', views.CartApiView.as_view(), name="cart"),
    path('cart/<int:pk>/',views.CartApiView.as_view(),),
]
