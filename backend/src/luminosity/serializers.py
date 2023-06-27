from rest_framework import serializers

from .models import Luminosity


class LuminosityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Luminosity
        fields = ("id", "date", "capteur", "intensite")


class LuminositySerializer(serializers.ModelSerializer):
    class Meta:
        model = Luminosity
        fields = ("id", "date", "capteur", "intensite")
