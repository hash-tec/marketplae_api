from rest_framework import serializers
from access.models import Customer
from .models import Product


class ProductSerializers(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name = "all", lookup_field = "pk")
    class Meta:
        model = Product
        exclude = ("slug", "date_created", 'image')


     
    def get_seller(self, obj):
        return obj.seller.email

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["seller"] = request.user
        return super().create(validated_data)
   

