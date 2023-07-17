from rest_framework_gis.filterset import GeoFilterSet

from .models import User


class UserFilter(GeoFilterSet):

    class Meta:
        model = User
        fields = ("id", "nom", "prenom", "email", "password")