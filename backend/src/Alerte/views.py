from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from .models import Alerte


class AlerteViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)
    queryset = Alerte.objects.all()


def alert_list(request):
    alerts = Alerte.objects.filter(is_resolved=False).order_by('-timestamp')
    return render(request, 'alert_list.html', {'alerts': alerts})
