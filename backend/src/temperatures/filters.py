from rest_framework_gis.filterset import GeoFilterSet

from .models import Temperature


class MoveFilter(GeoFilterSet):

    class Meta:
        model = Temperature
        fields = ("id", "salle_id", "temperature")