from rest_framework import viewsets

from api.models import GasStation
from api.serializers import GasStationSerializer


class GasStationViewSet(viewsets.ModelViewSet):
    queryset = GasStation.objects.all()
    serializer_class = GasStationSerializer
