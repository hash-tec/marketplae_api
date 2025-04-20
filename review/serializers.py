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

class AllReviewsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Review
        exclude = ['id']