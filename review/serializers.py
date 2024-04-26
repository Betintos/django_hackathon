from rest_framework import serializers
from .models import Review, Comment, User, Like, Favorite, Product, ReviewLike

# ===========================ОТЗЫВ===========================
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()
    liked_by_user = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'text', 'created_at', 'likes_count', 'liked_by_user']

    def get_likes_count(self, obj):
        return obj.reviewlike_set.count()

    def get_liked_by_user(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.reviewlike_set.filter(user=user).exists()
        return False

class ReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewLike
        fields = ['user', 'review']

#===========================КОММЕНТАРИИ===========================
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description']

class CommentSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'product', 'text', 'created_at', 'parent', 'likes_count', 'replies']

    def get_likes_count(self, obj):
        return obj.like_set.count()

    def get_replies(self, obj):
        replies = Comment.objects.filter(parent=obj)
        return CommentSerializer(replies, many=True).data

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'comment']

#===========================ЛАЙКИ===========================
class ProductSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    likes_detail = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'likes_count', 'likes_detail']

    def get_likes_count(self, obj):
        return obj.like_set.count()

    def get_likes_detail(self, obj):
        likes = Like.objects.filter(product=obj)
        return LikeSerializer(likes, many=True).data

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user']


#===========================ИЗБРАННОЕ===========================
class ProductSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'is_favorite']

    def get_is_favorite(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Favorite.objects.filter(user=user, product=obj).exists()
        return False

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user', 'product']
