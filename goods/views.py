from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer, ProductListSerializer
from .permissions import IsOwnerOrReadOnly

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['user']
    search_fields = ['name']

    def get_permissions(self):
        if self.action in ['list', 'retrive']:
            self.permission_classes = [AllowAny]
        elif self.action in ['create']:
            self.permission_classes = [IsAdminUser]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerOrReadOnly]
        elif self.action in ['purchase', 'add_to_cart']:
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return self.serializer_class
    
    def get_serializer_context(self):
        return {'request':self.request}
    
    def perform_create(self, serializer):
        image_file = self.request.data.get('image', None)
        if image_file:
            serializer.save(image=image_file)
        else:
            serializer.save()
        return Response('Продукт успешно создан', status=201)
    

