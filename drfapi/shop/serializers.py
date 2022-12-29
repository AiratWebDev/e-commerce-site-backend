from rest_framework import serializers
from .models import Product, ProductCatalog, Reviews


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCatalog
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
