from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import OrderViewSet, OrderConfirmationView

router = DefaultRouter()
router.register("orders", OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("orders/confirm_order/<str:email>/<str:confirmation_code>/", OrderConfirmationView.as_view(),
    name="confirm"),
]