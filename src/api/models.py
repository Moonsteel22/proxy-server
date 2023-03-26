from typing import Type

from django.db import models
from django.db.models import Model
from django.contrib.postgres.fields import ArrayField

from integration.logic.schemas import GasInfo, FuelInfo
from integration.logic.schemas import Service as ServiceSchema


# Create your models here.


class GasStation(Model):
    number = models.IntegerField(null=True, unique=True)
    address = models.CharField(max_length=255, null=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    urls = ArrayField(models.URLField(max_length=255), null=True)

    @classmethod
    def from_schema(cls: Type["GasStation"], schema: GasInfo):
        return cls(
            pk=schema.id,
            number=schema.number,
            address=schema.address,
            latitude=schema.coords.latitude,
            longitude=schema.coords.longitude,
            urls=schema.urls,
        )

    class Meta:
        ordering = ["number"]


class Service(Model):
    name = models.CharField(max_length=127)
    icon = models.ImageField(null=True)
    gas_station = models.ForeignKey(GasStation, on_delete=models.CASCADE)

    @classmethod
    def from_schema(
        cls: Type["Service"], gas_station: GasStation, schema: ServiceSchema
    ):
        return cls(name=schema.name, gas_station=gas_station)


class StationFuel(Model):
    price = models.DecimalField(max_digits=16, decimal_places=2)
    gas_station = models.ForeignKey(GasStation, on_delete=models.CASCADE)
    currency = models.CharField(max_length=31, default="roubles")
    name = models.CharField(max_length=127, null=True)
    icon = models.ImageField(null=True)

    @classmethod
    def from_schema(cls, gas_station_id: int, schema: FuelInfo):
        return cls(
            price=schema.price.value,
            gas_station_id=gas_station_id,
            name=schema.name,
            currency=schema.currency,
        )
