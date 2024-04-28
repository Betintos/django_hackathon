from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import filters, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Order
from .serializers import *
from goods.permissions import IsOwnerOrReadOnly
from account.serializers import EmailSerializer


User = get_user_model()

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ["user"]
    search_fields = ["pk"]

    def get_permissions(self):
        if self.action in ['list', 'retrive']:
            self.permission_classes = [AllowAny]
        elif self.action in ['create']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in self.permission_classes]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        return self.serializer_class
    
    def get_serializer_context(self):
        return {'request': self.request}

    def perform_create(self, serializer):
        serializer.save()
        return Response("Ваш заказ ждёт подтвержения", 201)


class OrderConfirmationView(generics.GenericAPIView):
    def get(self, request, email, confirmation_code):
        user = User.objects.filter(email=email).first()
        if not user:
            return Response("Пользователь не найден", 404)

        order = Order.objects.filter(confirmation_code=confirmation_code).first()
        if not order:
            return Response("Заказ не найден", 404)

        order.confirmation_code = ""
        order.is_confirmed = True
        order.save()
        return Response("Ваш заказ подтверждён")