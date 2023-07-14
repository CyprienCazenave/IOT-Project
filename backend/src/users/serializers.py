from rest_framework import serializers

from .models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "nom", "prenom","Email","password")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "nom", "prenom","Email","password")
