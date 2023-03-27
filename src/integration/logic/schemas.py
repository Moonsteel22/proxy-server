from dataclasses import dataclass


@dataclass
class Coordinates:
    """
    Координаты. Ширина и долгота
    """

    def __init__(self, latitude: float, longitude: float):
        self._longitude = longitude
        self._latitude = latitude

    @property
    def latitude(self):
        return self._latitude.__round__(5)

    @property
    def longitude(self):
        return self._longitude.__round__(5)


@dataclass
class Money:
    def __init__(self, value: float):
        self._value = value

    @property
    def value(self):
        return self._value.__round__(2)

    def __str__(self):
        return f"{self.value}"


@dataclass
class Service:
    name: str


@dataclass
class GasInfo:
    """
    Информация об АЗС.
    """

    id: int
    number: int
    coords: Coordinates
    address: str
    urls: list[str]
    services: list[Service]


@dataclass
class FuelInfo:
    """
    Информация о топливе
    """

    name: str
    price: Money
    currency: str


@dataclass
class StationFuelInfo:
    """
    Список топлива в АЗС
    """

    id: int
    fuels: list[FuelInfo]
