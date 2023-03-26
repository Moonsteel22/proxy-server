import random
from typing import Generator

from integration.logic.schemas import FuelInfo
from integration.logic.schemas import StationFuelInfo, Money
from integration.logic.sources.first_source import GAS_STATION_EXPONENT

FUEL_EXPONENT = 10


class SecondSource:
    @staticmethod
    def get_data() -> Generator[StationFuelInfo, None, None]:
        _fuel_types = [f"Fuel - {i}" for i in range(1, FUEL_EXPONENT * 10 - 1)]
        return (
            StationFuelInfo(
                id=random.randint(1, GAS_STATION_EXPONENT * 2),
                fuels=[
                    FuelInfo(
                        name=random.choice(_fuel_types),
                        price=Money(random.randint(40, 80) + random.random()),
                        currency="roubles",
                    )
                    for _ in range(FUEL_EXPONENT)
                ],
            )
            for _ in range(GAS_STATION_EXPONENT)
        )
