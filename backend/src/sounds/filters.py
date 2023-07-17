from rest_framework_gis.filterset import GeoFilterSet

from .models import Sounds


class SoundsFilter(GeoFilterSet):

    class Meta:
        model = Sounds
        fields = ("id", "salle_id", "sound")
