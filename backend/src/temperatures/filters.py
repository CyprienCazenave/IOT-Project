from rest_framework_gis.filterset import GeoFilterSet

from .models import Temperatures


class TemperatureFilter(GeoFilterSet):

    class Meta:
        model = Temperatures
        fields = ("id", "salle_id", "temperature")