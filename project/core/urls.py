from rest_framework.routers import DefaultRouter

from .views import (
    AddressViewSet,
    CategoryViewSet,
    GlobalCounterViewSet,
    ItemViewSet,
    OrderItemViewSet,
    OrderViewSet,
    PaymentViewSet,
    UserProfileViewSet,
    ItemAndCategoryViewSet,
)

router = DefaultRouter()

router.register(r"items", ItemViewSet)
router.register(
    r"items-and-categories", ItemAndCategoryViewSet, basename="items-and-categories"
)
router.register(r"categories", CategoryViewSet)
router.register(r"orders", OrderViewSet)
router.register(r"order-items", OrderItemViewSet)
router.register(r"addresses", AddressViewSet)
router.register(r"payments", PaymentViewSet)
router.register(r"user-profiles", UserProfileViewSet)
router.register(r"global-counters", GlobalCounterViewSet)

urlpatterns = router.urls
