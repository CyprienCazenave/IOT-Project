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
from django.urls import include, path, reverse_lazy
from rest_framework import routers
import sys

from cours.views import CoursViewSet
from events.views import EventsViewSet
from luminosity.views import LuminosityViewSet
from users.views import UserViewSet
from moves.views import MoveViewSet
from rooms.views import RoomViewSet
from sounds.views import SoundViewSet
from temperatures.views import TemperatureViewSet


sys.path.append("..")


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
    # Wire up our API using automatic URL routing.
    # rest_framework api routing
    path("api/", include(ROUTER.url)),
    # This requires login for put/update while allowing get (read-only) for everyone.
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('admin/', admin.site.urls),
]
