from rest_framework import serializers

from .models import User


class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "nom", "prenom","Email","password")


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "nom", "prenom","Email","password")
