from rest_framework import serializers

from .models import Temperature


class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ("id", "salle_id", "temperature")


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ("id", "salle_id", "temperature")