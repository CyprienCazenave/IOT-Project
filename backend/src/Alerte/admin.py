from django.contrib import admin


from models import Alerte


@admin.register(Alerte)
class LuminosityAdmin(admin.ModelAdmin):
    list_display = (
        "alert_type)",
        "description",
        "timestamp",
        "is_resolved",
    )
