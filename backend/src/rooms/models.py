import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel


class Room(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    max_capacity = models.IntegerField(null=True, blank=True)
