from django.urls import path

from .views import GetProductsView, CreateProductView

urlpatterns = [
    path('products/', GetProductsView.as_view()),
    path('post_product/', CreateProductView.as_view())
]