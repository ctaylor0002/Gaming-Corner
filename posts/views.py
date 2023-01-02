from rest_framework import status
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# I need to make a way to get posts based on a user aswell
@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_posts(request, user_id):
    posts = Post.objects.filter(user=user_id)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Like or dislike the post
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def like_or_dislike_post(request, pk):
    #Add a param for like or dislike
    like_or_dislike_param = request.query_params.get('type')
    post = get_object_or_404(Post, pk=pk)

    if like_or_dislike_param == 'like':
        post.likes = (post.likes) + 1
    
    elif like_or_dislike_param == 'dislike':
        post.dislikes = (post.dislikes) + 1
    
    post.save()

    serializer = PostSerializer(post)

    return Response(serializer.data, status=status.HTTP_200_OK)

    