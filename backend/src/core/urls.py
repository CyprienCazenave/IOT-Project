"""ProjectIOT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import user_passes_test
from django.urls import include, path, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from fobi.contrib.apps.drf_integration.urls import fobi_router
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from backend.src.cours.views import CoursViewSet
from backend.src.events.views import EventsViewSet
from backend.src.luminosity.views import LuminosityViewSet
from backend.src.users.views import UserViewSet
from backend.src.moves.views import MoveViewSet
from backend.src.rooms.views import RoomViewSet
from backend.src.sounds.views import SoundViewSet
from backend.src.temperatures.views import TemperatureViewSet


class OptionalSlashRouter(routers.DefaultRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trailing_slash = "/?"


ROUTER = OptionalSlashRouter()
ROUTER.register(r"cours", CoursViewSet, basename="cours")
ROUTER.register(r"events", EventsViewSet, basename="events")
ROUTER.register(r"luminosity", LuminosityViewSet, basename="luminosity")
ROUTER.register(r"users", UserViewSet, basename="user")
ROUTER.register(r"moves", MoveViewSet, basename="move")
ROUTER.register(r"rooms", RoomViewSet, basename="rooms")
ROUTER.register(r"sounds", SoundViewSet, basename="sounds")
ROUTER.register(r"temperature", TemperatureViewSet, basename="temperature")


urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('admin/', admin.site.urls),
]
