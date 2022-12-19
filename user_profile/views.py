from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes


# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def create_profile(request):
    print(request.user)
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)