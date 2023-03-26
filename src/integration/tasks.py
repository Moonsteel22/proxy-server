from faker import Faker
from integration.logic.sources.first_source import FirstSource
from integration.logic.sources.second_source import SecondSource
from api.models import GasStation, Service, StationFuel


def second_source_import_task():
    _batch = 4096

    source_handler = SecondSource()

    objects = source_handler.get_data()

    fuels = []
    for item in objects:

        fuels.extend(
            [
                StationFuel.from_schema(gas_station_id=item.id, schema=fuel)
                for fuel in item.fuels
            ]
        )
        if _batch % len(fuels) == 0:
            StationFuel.objects.bulk_create(fuels)
            fuels = []
    StationFuel.objects.bulk_create(fuels)


def first_source_import_task():
    _batch = 4096

    fake = Faker()

    source_handler = FirstSource(fake=fake)
    objects = source_handler.get_data()

    gas_stations, services = [], []
    counter = 0
    for item in objects:

        gas_station = GasStation.from_schema(schema=item)
        gas_stations.append(gas_station)
        services.extend(
            [Service(gas_station=gas_station, name=i.name) for i in item.services]
        )

        counter += 1
        if _batch % counter == 0:
            GasStation.objects.bulk_create(gas_stations, ignore_conflicts=True)

            Service.objects.bulk_create(services, ignore_conflicts=True)
            gas_stations, services = [], []

    GasStation.objects.bulk_create(gas_stations, ignore_conflicts=True)
    Service.objects.bulk_create(services, ignore_conflicts=True)
