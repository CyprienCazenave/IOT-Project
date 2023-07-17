from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import Cours
from .filters import CoursFilter
from .serializers import CoursSerializer, CoursListSerializer


class CoursViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = IsAuthenticated
    filterset_class = CoursFilter
    queryset = Cours.objects.all()

    def get_queryset(self):
        """
        Get all the companies related to the authenticated user.
        """
        if self.request.user.is_superuser:
            return Cours.objects.all()
        return Cours.objects.filter()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CoursSerializer
        return CoursListSerializer

    def create(self, request, *args, **kwargs):
        """
        Some geometries are so huge that they can't pass through the GET parameter.
        That's why we allow the client to filter the API passing the URL parameters in
        a POST request.

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        f = self.filterset_class(request.data, self.get_queryset())
        serializer = self.get_serializer(f.qs, many=True)
        return Response(serializer.data)
