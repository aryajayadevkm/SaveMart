from rest_framework import serializers

from .models import (
    Shop,
    Product,
    ProductShop,
)


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductShop
        fields = '__all__'