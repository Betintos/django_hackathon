from django.urls import path

from .views import ProductViewSet



urlpatterns = [
    path('', ProductViewSet.as_view()),
     path('image/<str:image_name>/', ProductViewSet.as_view(), name='image-view')
]