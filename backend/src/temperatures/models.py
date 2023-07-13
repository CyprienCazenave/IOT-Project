import uuid

from django.db import models
from django_extensions.db.models import TimesStampedModel


class temperatures(TimesStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    salle_id = models.CharField(max_length=255, null=True, blank=True)
    temperature = models.CharField(max_length=255, null=True, blank=True)