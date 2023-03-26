from rest_framework import serializers
from api.models import GasStation, Service, StationFuel


class StationFuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationFuel
        fields = ["price", "currency", "name"]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["name"]


class GasStationSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    station_fuels = StationFuelSerializer(many=True, read_only=True)

    class Meta:
        model = GasStation
        fields = [
            "number",
            "address",
            "latitude",
            "longitude",
            "urls",
            "services",
            "station_fuels",
        ]
