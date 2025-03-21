from rest_framework import serializers 

from .models import Item 


from django.contrib.auth import get_user_model 

from rest_framework.validators import UniqueValidator 

from django.contrib.auth.password_validation import validate_password 
 

class ItemSerializer(serializers.ModelSerializer): 

    class Meta: 

        model = Item 

        fields = '__all__' 

User = get_user_model() 

 
class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user


