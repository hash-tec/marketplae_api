from django.urls import path
from .views import RegisterUserApiView


urlpatterns = [
    path('register/', RegisterUserApiView.as_view(), name = "register"),
]
