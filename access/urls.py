from django.urls import path
from .views import RegisterUserApiView, Testing


urlpatterns = [
    path('register/', RegisterUserApiView.as_view(), name = "register"),
    path('testing/', Testing.as_view(), name = "testing_a")
]
