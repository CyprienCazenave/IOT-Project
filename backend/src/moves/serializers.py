from rest_framework import serializers

from .models import Move


class MoveListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ("id", "date", "room_id", "nb_person")


class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ("id", "date", "room_id", "nb_person")
