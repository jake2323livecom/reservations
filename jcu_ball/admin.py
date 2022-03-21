from django.contrib import admin
from .models import BallReservation


@admin.register(BallReservation)
class BallReservationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'chicken', 'beef', 'fish', 'created_by')