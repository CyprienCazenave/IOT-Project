from django.contrib import admin


from .models import Temperature


@admin.register(Temperature)
class MoveAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "salle_id",
        "temperature",
        
    )
