from rest_framework import serializers
from .models import Review


class ReviewSerializers(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['reviewer', 'comment', 'rating']



        # def save(self, validated_data = None);
        #     request = self.context.get("request")
        #     vali