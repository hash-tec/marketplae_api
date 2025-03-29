from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet
from cart.views import CartViewset

routers = DefaultRouter()
routers.register('products', ProductViewSet, basename= "products" )
routers.register('cart', CartViewset, basename="cartup")

urlpatterns = routers.urls