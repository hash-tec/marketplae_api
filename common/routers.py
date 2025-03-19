from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet

routers = DefaultRouter()
routers.register('products', ProductViewSet, basename= "products" )

urlpatterns = routers.urls