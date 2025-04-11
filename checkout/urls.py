from django.urls import path
from .views import CheckoutApiView

urlpatterns = [
    path('',CheckoutApiView.as_view() )
]
