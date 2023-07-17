from rest_framework import serializers

from .models import Temperatures


class TemperatureListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperatures
        fields = ("id", "salle_id", "temperature")


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperatures
        fields = ("id", "salle_id", "temperature")