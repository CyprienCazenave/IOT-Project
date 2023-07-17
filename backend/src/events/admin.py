from django.contrib import admin


from .models import Events


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "salle_id",
        "date_debut",
        "date_fin",
    )