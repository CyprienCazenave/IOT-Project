from rest_framework_gis.filterset import GeoFilterSet

from .models import Events


class EventsFilter(GeoFilterSet):

    class Meta:
        model = Events
        fields = ("id", "salle_id", "date_debut", "date_fin")
