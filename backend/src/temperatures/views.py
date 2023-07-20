from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import Temperatures
from .filters import TemperatureFilter
from .serializers import TemperatureSerializer, TemperatureListSerializer


class TemperatureViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)
    filterset_class = TemperatureFilter
    queryset = Temperatures.objects.all()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Temperatures.objects.all()
        return Temperatures.objects.filter()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return TemperatureSerializer
        return TemperatureListSerializer

    def create(self, request, *args, **kwargs):

        f = self.filterset_class(request.data, self.get_queryset())
        serializer = self.get_serializer(f.qs, many=True)
        return Response(serializer.data)
