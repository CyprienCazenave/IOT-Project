from rest_framework import serializers

from .models import Cours


class CoursListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = ("id", "salle_id", "date_debut", "date_fin")


class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = ("id", "salle_id", "date_debut", "date_fin")
