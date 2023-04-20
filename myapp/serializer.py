from rest_framework import serializers
from .models import *
from .models import Product

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name')

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['employee','department']

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock2
        fields = ['symbol','price','currency']

# class SampleUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SampleUser
#         fields = ['name', 'surname', 'email', 'password', 'last_login']