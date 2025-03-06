from rest_framework import serializers
from access.models import Customers
from .models import Products


class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        exclude = ("seller", "slug", "date_created")

        # def create(self, validated_data):
        #     request = self.context.get("request")
        #     if request and validated_data(request, "user"):
        #         validated_data["seller"] = request.user
        #     return super().create(validated_data)


