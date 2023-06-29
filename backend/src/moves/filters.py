from rest_framework_gis.filterset import GeoFilterSet

from .models import Move


class MoveFilter(GeoFilterSet):

    class Meta:
        model = Move
        fields = ("name", "date", "room_id", "nb_person")
