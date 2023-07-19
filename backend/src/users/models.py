import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import UserManager


class User(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    nom = models.CharField(max_length=255, null=True, blank=True, unique=True)
    prenom = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = 'nom'
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    @staticmethod
    def is_authenticated(self):
        return False
