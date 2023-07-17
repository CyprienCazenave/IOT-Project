from django.contrib import admin


from .models import Temperatures


@admin.register(Temperatures)
class TemperatureAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "salle_id",
        "temperature",
    )
