from rest_framework import serializers
from .models import Coupon
from string import ascii_uppercase, digits
from random import choices

class CouponSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only = True)
    code = serializers.CharField(read_only = True)
    identifier = serializers.CharField(read_only = True)

    class Meta:
        model = Coupon
        exclude = ("date_created",)


    def create(self, validated_data):
        request = self.context.get("request")
        validated_data['user'] = request.user
        validated_data['code'] = ''.join(choices( ascii_uppercase + digits, k=7))
        if validated_data['coupon_name'].lower()== "product coupon":
            validated_data['identifier'] = "PC"
        elif validated_data['coupon_name'].lower()== "new user coupon":
            validated_data['identifier'] = "NUC"
        return super().create(validated_data)
    
