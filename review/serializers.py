from rest_framework import serializers
from .models import Review
from products.models import Product


class ReviewSerializers(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = [ 'comment', 'rating']


        def save(self, validated_data = None, **kwargs):
            request = self.context.get("request")
            validated_data['reviewer'] = request.user.get_full_name()
            return super().create(validated_data)