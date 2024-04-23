from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product
from .serializers import ProductSerializer


class GetProductsView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializers = ProductSerializer(data=queryset, many=True)
        serializers.is_valid()
        return Response(serializers.data)
    
class CreateProductView(APIView):
    def post(self, request):
        category_ = Category.objects.get(id=request.data['category'])
        product = Product.objects.create(
            name = request.data['name'],
            price = request.data['price'],
            category = category_
        )
        return Response('Успешно создано!')