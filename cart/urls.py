from django.urls import path
from .views import CartApiView
urlpatterns = [
    path('', CartApiView.as_view()),
]
