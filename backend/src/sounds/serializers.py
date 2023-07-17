from rest_framework import serializers

from .models import Sounds


class SoundListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sounds
        fields = ("id", "salle_id", "sound")


class SoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sounds
        fields = ("id", "salle_id", "sound")
