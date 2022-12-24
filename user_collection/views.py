from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import UserCollection
from .serializers import UserCollectionSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes


# Create your views here.
        
@api_view(['GET'])
@permission_classes([AllowAny])
def get_collection(request, user_id):
    collection = get_object_or_404(UserCollection, user=user_id)
    # profile = UserProfile.objects.filter(pk=pk)
    print(collection)
    serializer = UserCollectionSerializer(collection)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)