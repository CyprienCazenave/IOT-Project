from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import Room
from .serializers import RoomSerializer, RoomListSerializer


class RoomViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)
    queryset = Room.objects.all()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Room.objects.all()
        return Room.objects.filter()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return RoomSerializer
        return RoomListSerializer

    def create(self, request, *args, **kwargs):
        f = self.filterset_class(request.data, self.get_queryset())
        serializer = self.get_serializer(f.qs, many=True)
        return Response(serializer.data)
