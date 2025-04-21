from rest_framework import serializers
from .models import Customer, Address
class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only = True)
    class Meta:
        model = Customer
        fields = ["id","first_name","last_name", "email","password", "password2", "gender"]
        #extra_kwargs changes the field to being a write only field
        extra_kwargs = {"password":{'write_only': True}}


    #validate the password against  
    def validate(self, data):
            if data['password2'] != data["password"]:
                raise serializers.ValidationError("Passwords doesn't match")
            return data
        
    def create(self, validated_data):
        validated_data.pop("password2")
        user = Customer.objects.create_user(**validated_data)
        return user
    
class AddressSerializer(serializers.ModelSerializer):
     
    class Meta:
          model = Address
          exclude = ("customer","id",)
          
    def save(self, validated_data = None):
        if validated_data is None:
             validated_data = self.validated_data
        request = self.context.get("request")
        validated_data['customer'] = request.user
        return super().create(validated_data)
        