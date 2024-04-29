from rest_framework import viewsets, generics
from .models import Review, Comment, Like, Favorite, Product, ReviewLike, Rating
from .serializers import ReviewSerializer, CommentSerializer, LikeSerializer, FavoriteSerializer, ProductSerializer, ReviewLikeSerializer, RatingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from . import models
#===========================ОТЗЫВ===========================
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewLikeViewSet(viewsets.ModelViewSet):
    queryset = ReviewLike.objects.all()
    serializer_class = ReviewLikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


#===========================КОММЕНТАРИИ===========================
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#===========================ЛАЙКИ===========================
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

#===========================ИЗБРАННОЕ===========================
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ===========================РЕЙТИНГ===========================
# class TopRatedProductList(generics.ListAPIView):
#     queryset = Product.objects.annotate(avg_rating=models.Avg('reviews__rating')).order_by('-avg_rating')
#     serializer_class = ProductSerializer

class RatingCreateAPIView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RatingListAPIView(generics.ListAPIView):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()