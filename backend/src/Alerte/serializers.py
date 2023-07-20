from rest_framework import serializers

from models import Alerte


class AlerteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerte
        fields = ("alert_type", "description", "timestamp","is_resolved")


class AlerteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerte
        fields = ("alert_type", "description", "timestamp", "is_resolved")
