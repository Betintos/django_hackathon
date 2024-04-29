from django.utils.crypto import get_random_string
from rest_framework import serializers

from .models import Order
from .utils import send_order_confirmation_code

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["user"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        order = super().create(validated_data)
        order.confirmation_code = get_random_string(length=10, allowed_chars="1234567890")
        send_order_confirmation_code(order.user.email, order.confirmation_code)
        order.save()
        return order


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["pk", "total_amount", "is_confirmed"]
