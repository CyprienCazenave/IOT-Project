from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import Events
from .filters import EventsFilter
from .serializers import EventsSerializer, EventsListSerializer


class EventsViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = IsAuthenticated
    filterset_class = EventsFilter
    queryset = Events.objects.all()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Events.objects.all()
        return Events.objects.filter()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return EventsSerializer
        return EventsListSerializer

    def create(self, request, *args, **kwargs):
        f = self.filterset_class(request.data, self.get_queryset())
        serializer = self.get_serializer(f.qs, many=True)
        return Response(serializer.data)
