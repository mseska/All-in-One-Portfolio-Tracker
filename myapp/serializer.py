from rest_framework import serializers
from .models import *



class UserSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = User
    #     fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
    #     extra_kwargs = {
    #         'password': {'write_only': True}
    #     }

    class Meta:
        model = User
        fields = ('id', 'password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }
    # def create(self, validated_data):
    #     user = User.objects.create_user(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name'],
    #         password=validated_data['password']
    #     )
    #     return user