import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel


class Temperatures(TimeStampedModel):
    # mettre à jour avec les vrais données d'un  capteur de type temperature
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    salle_id = models.CharField(max_length=255, null=True, blank=True)
    temperature = models.CharField(max_length=255, null=True, blank=True)