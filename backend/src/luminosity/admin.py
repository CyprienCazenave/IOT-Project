from django.contrib import admin


from luminosity.models import Luminosity


@admin.register(Luminosity)
class LuminosityAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "date",
        "capteur",
        "intensite",
    )
