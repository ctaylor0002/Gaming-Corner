from rest_framework import serializers
from .models import UserCollection

class UserCollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCollection
        fields = ['user', 'video_game', 'completed']
        depth = 1