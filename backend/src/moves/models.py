import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel


class Move(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    date = models.DateField()
    room_id = models.CharField(max_length=255, null=True, blank=True)
    nb_person = models.CharField(max_length=45, null=True, blank=True)
