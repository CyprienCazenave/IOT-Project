from rest_framework import serializers

from .models import Events


class CoursListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ("id", "salle_id", "date_debut", "date_fin")


class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ("id", "salle_id", "date_debut", "date_fin")
        
