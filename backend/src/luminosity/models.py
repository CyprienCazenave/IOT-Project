import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel


class Luminosity(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    date = models.DateField()
    capteur = models.CharField(max_length=255, null=True, blank=True)
    intensite = models.FloatField()
