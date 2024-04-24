from django.urls import path

from .views import GetProductsView, CreateProductView, product_detail

urlpatterns = [
    path('products/', GetProductsView.as_view()),
    path('post_product/', CreateProductView.as_view()),
    path('get_product/<int:id>/', product_detail)
]