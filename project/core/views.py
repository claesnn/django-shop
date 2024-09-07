"""Views for the core app."""

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

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
from .serializers import (
    AddressSerializer,
    CategorySerializer,
    GlobalCounterSerializer,
    ItemSerializer,
    ItemAndCategorySerializer,
    OrderItemSerializer,
    OrderSerializer,
    PaymentSerializer,
    UserProfileSerializer,
)


# Create your views here.
class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemAndCategoryViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemAndCategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class GlobalCounterViewSet(ModelViewSet):
    queryset = GlobalCounter.objects.all()
    serializer_class = GlobalCounterSerializer

    @action(detail=True, methods=["post"])
    def increment(self, request, pk=None):
        counter = self.get_object()
        counter.increment()
        serializer = self.get_serializer(counter)
        return Response(serializer.data)
