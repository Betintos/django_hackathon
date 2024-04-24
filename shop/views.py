from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

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
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response('Такой продукт уже существует!')
    
@api_view(['GET'])
def product_detail(request, id):
    product = get_object_or_404(Product,id=id)
    serializers = ProductSerializer(instance=product)
    return Response(serializers.data)