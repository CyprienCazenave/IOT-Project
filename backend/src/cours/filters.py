from rest_framework_gis.filterset import GeoFilterSet

from .models import Cours


class CoursFilter(GeoFilterSet):

    class Meta:
        model = Cours
        fields = ("id", "salle_id", "date_debut", "date_fin")
