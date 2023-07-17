from django.contrib import admin


from .models import Sounds


@admin.register(Sounds)
class SoundsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "salle_id",
        "sound",
    )
