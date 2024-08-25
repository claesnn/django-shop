"""This module contains the serializers for the core app."""

from rest_framework.serializers import ModelSerializer

from .models import (
    Address,
    Category,
    GlobalCounter,
    Item,
    Order,
    OrderItem,
    Payment,
    UserProfile,
)


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        depth = 1


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ["items", "ordered", "created_at", "payment"]


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class GlobalCounterSerializer(ModelSerializer):
    class Meta:
        model = GlobalCounter
        fields = ["id", "count", "last_updated"]
        read_only_fields = ["count", "last_updated"]
