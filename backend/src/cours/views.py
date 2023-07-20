from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import Cours
from .serializers import CoursSerializer, CoursListSerializer


class CoursViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = IsAuthenticated
    queryset = Cours.objects.all()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Cours.objects.all()
        return Cours.objects.filter()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CoursSerializer
        return CoursListSerializer

    def create(self, request, *args, **kwargs):
        f = self.filterset_class(request.data, self.get_queryset())
        serializer = self.get_serializer(f.qs, many=True)
        return Response(serializer.data)
