from django.urls import path
from . import views
urlpatterns = [
    path('cart/', views.CartViewset.as_view({'get':'list'}), name="cart"),
    path('cart/',views.CartViewset.as_view({'post': 'post'})),
]
