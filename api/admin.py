from django.contrib import admin
from django.contrib.admin import ModelAdmin
from models import GasStation, Service, Fuel, StationFuel


@admin.register(GasStation)
class GasStationAdmin(ModelAdmin):
    ...


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    ...


@admin.register(Fuel)
class FuelAdmin(ModelAdmin):
    ...


@admin.register(StationFuel)
class StationFuelAdmin(ModelAdmin):
    ...
