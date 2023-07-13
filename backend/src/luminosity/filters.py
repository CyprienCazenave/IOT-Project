from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter

from .models import Luminosity


class LuminosityFilter(GeoFilterSet):

    class Meta:
        model = Luminosity
        fields = ("name", "date", "room_id", "intensite")
