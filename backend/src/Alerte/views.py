from django.shortcuts import render
from models import Alerte


def alert_list(request):
    alerts = Alerte.objects.filter(is_resolved=False).order_by('-timestamp')
    return render(request, 'alert_list.html', {'alerts': alerts})
