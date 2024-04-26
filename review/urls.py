from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, ProductViewSet, LikeViewSet, FavoriteViewSet, ReviewLikeViewSet, ReviewViewSet


# ===========================ОТЗЫВ===========================
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'review-likes', ReviewLikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

#===========================КОММЕНТАРИИ===========================
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

#===========================ЛАЙКИ===========================
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

#===========================ИЗБРАННОЕ===========================
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'favorites', FavoriteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]