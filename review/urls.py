from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, ProductViewSet, LikeViewSet, FavoriteViewSet, ReviewLikeViewSet, ReviewViewSet, RatingCreateAPIView, RatingListAPIView


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

# ===========================РЕЙТИНГ===========================
# urlpatterns = [
#     path('top-rated-products/', TopRatedProductList.as_view(), name='top-rated-products'),
# ]

urlpatterns = [
    path('ratings/', RatingCreateAPIView.as_view(), name='rating-create'),
    path('ratings/<int:pk>/', RatingListAPIView.as_view(), name='rating-list'),
]