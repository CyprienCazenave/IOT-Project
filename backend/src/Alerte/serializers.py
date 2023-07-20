from rest_framework import serializers

from .models import Alertes


class AlertesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alertes
        fields = ("alert_type", "description", "timestamp","is_resolved")


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alertes 
        fields = ("alert_type", "description", "timestamp", "is_resolved")
