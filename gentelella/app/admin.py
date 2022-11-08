from django.contrib import admin

from . import models
# Register your models here.

@admin.register(models.Meter)
class MeterAdmin(admin.ModelAdmin):

    list_display = ['id', 'meter_id', 'name']


@admin.register(models.Control)
class ControlAdmin(admin.ModelAdmin):

    list_display = ['control_id', 'name']