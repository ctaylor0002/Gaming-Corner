from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'post_content', 'likes', 'dislikes']
        depth = 1
