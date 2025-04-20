from django.urls import path
from . import views

urlpatterns = [
    path('',views.CheckoutApiView.as_view() ),
    path('address/',views.ShippingAddress.as_view() ),
    path('payment/', views.OrderApiView.as_view()),
    path('address/<int:id>',views.ShippingAddress.as_view() ),
]
