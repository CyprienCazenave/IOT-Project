from django.contrib import admin


from .models import Move


@admin.register(Move)
class MoveAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "date",
        "room_id",
        "nb_person",
    )
