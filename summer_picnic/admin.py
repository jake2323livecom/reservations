from django.contrib import admin
from .models import PicnicReservation


@admin.register(PicnicReservation)
class PicnicReservationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'comments', 'created_by')