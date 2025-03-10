from rest_framework import serializers
from .models import Customer
class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only = True)
    class Meta:
        model = Customer
        fields = ["first_name","last_name", "email","password", "password2", "gender"]
        extra_kwargs = {"password":{'write_only': True}}

    def validate(self, data):
            if data['password'] != data["password2"]:
                raise serializers.ValidationError({"password2": "Passwords must match"})
            return data
        
    def create(self, validated_data):
            validated_data.pop("password2")
            user = Customer.objects.create_user(**validated_data)
            return user