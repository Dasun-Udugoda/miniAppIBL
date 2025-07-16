from rest_framework import serializers
from .models import BlogPost, ReviewPost

class BlogPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id", "title","content", "created_at"]


class ReviewPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReviewPost
        fields = ["id", "title","content", "created_at"]