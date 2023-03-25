from django.db import models
from django.db.models import Model
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class GasStation(Model):
    number = models.IntegerField()
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(decimal_places=5, null=True)
    longitude = models.DecimalField(decimal_places=5, null=True)
    urls = ArrayField(models.URLField(max_length=255))

    class Meta:
        ordering = ["number"]


class Service(Model):
    name = models.CharField(max_length=127)
    icon = models.ImageField(null=True)
    gas_station = models.ForeignKey(GasStation, on_delete=models.CASCADE)


class Fuel(Model):
    name = models.CharField(max_length=127)
    icon = models.ImageField(null=True)
    currency = models.CharField(max_length=31)


class StationFuel(Model):
    price = models.DecimalField(decimal_places=2)
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    gas_station = models.ForeignKey(GasStation, on_delete=models.CASCADE)
