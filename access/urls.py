from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterUserApiView.as_view(), name = "register"),
    path('address/',views.AddressApiView.as_view() ),
    path('address/<int:pk>/',views.AddressApiView.as_view() ),
]
