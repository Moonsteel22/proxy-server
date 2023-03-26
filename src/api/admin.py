from django.contrib import admin
from django.contrib.admin import ModelAdmin
from api.models import GasStation, Service, StationFuel


@admin.register(GasStation)
class GasStationAdmin(ModelAdmin):
    ...


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    ...


@admin.register(StationFuel)
class StationFuelAdmin(ModelAdmin):
    ...
