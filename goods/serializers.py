from rest_framework import serializers

from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        product = super().create(validated_data)
        product.save()
        return product
    
    
class ProductListSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Product
        fields = ['name', 'price', 'image']


