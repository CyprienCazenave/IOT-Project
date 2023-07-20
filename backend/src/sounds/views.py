from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import Sounds
from .filters import SoundsFilter
from .serializers import SoundSerializer, SoundListSerializer


class SoundViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)
    filterset_class = SoundsFilter
    queryset = Sounds.objects.all()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Sounds.objects.all()
        return Sounds.objects.filter()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return SoundSerializer
        return SoundListSerializer

    def create(self, request, *args, **kwargs):

        f = self.filterset_class(request.data, self.get_queryset())
        serializer = self.get_serializer(f.qs, many=True)
        return Response(serializer.data)
