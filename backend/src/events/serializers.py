from rest_framework import serializers

from .models import Events


class EventsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ("id", "salle_id", "date_debut", "date_fin")


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ("id", "salle_id", "date_debut", "date_fin")
        
