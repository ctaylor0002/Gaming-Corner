from rest_framework import status
from rest_framework.response import Response
from .models import UserFollowers
from .serializers import UserFollowerSerializer
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def following(request):
    following = UserFollowers.objects.filter(main_user_id = request.user.id)
    serializer = UserFollowerSerializer(following, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def followers(request):
    followers = UserFollowers.objects.filter(follower_user_id = request.user.id)
    serializer = UserFollowerSerializer(followers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)