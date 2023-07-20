from django.shortcuts import render
from .models import Alert


def alert_list(request):
    alerts = Alert.objects.filter(is_resolved=False).order_by('-timestamp')
    return render(request, 'alert_list.html', {'alerts': alerts})
