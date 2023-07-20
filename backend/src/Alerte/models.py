# models.py

from django.db import models

class Alert(models.Model):
    ALERT_TYPES = (
        ('Temperature', 'Temperature'),
        # Ajoutez d'autres types d'alerte selon vos besoins
    )

    alert_type = models.CharField(max_length=50, choices=ALERT_TYPES)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.alert_type} - {self.timestamp}"
