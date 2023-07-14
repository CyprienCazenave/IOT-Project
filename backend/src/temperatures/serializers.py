from rest_framework import serializers

from .models import Temperature


class TemperatureListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ("id", "salle_id", "temperature")


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ("id", "salle_id", "temperature")