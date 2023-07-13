import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel


class users(TimeStampedModel):
    id  =models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    nom = models.CharField(max_length=255, null=True, blank=True)
    prenom = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)