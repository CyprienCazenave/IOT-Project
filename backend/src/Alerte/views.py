from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from .models import Alerte
from .serializers import AlerteSerializer, AlerteListSerializer


class AlerteViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)

    queryset = Alerte.objects.all()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Alerte.objects.all()
        return Alerte.objects.filter()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return AlerteSerializer
        return AlerteListSerializer

    def create(self, request, *args, **kwargs):
        f = self.filterset_class(request.data, self.get_queryset())
        serializer = self.get_serializer(f.qs, many=True)
        return Response(serializer.data)


def alert_list(request):
    alerts = Alerte.objects.filter(is_resolved=False).order_by('-timestamp')
    return render(request, 'alert_list.html', {'alerts': alerts})

