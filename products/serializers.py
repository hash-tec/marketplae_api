from rest_framework import serializers
from access.models import Customers
from .models import Products


class ProductsSerializers(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField()
    class Meta:
        model = Products
        exclude = ("slug", "date_created", 'image')


     
    def get_seller(self, obj):
        return obj.seller.email

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["seller"] = request.user
        return super().create(validated_data)
   

