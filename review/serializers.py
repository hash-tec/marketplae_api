from rest_framework import serializers
from .models import Review
from products.models import Product


class ReviewSerializers(serializers.ModelSerializer):

    class Meta:
        model = Review
        exclude = ["product"]

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating is between 1 and 5")
        return value
    def save(self, validated_data= None): 
        if validated_data is None:
            validated_data = self.validated_data
        request = self.context.get('request')
        validated_data['reviewer'] = request.user
        return super().create(validated_data)
class AllReviewsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"