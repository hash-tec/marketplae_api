from django.urls import path
from . import views


urlpatterns = [
    path('', views.ReviewsApiView.as_view())
]
