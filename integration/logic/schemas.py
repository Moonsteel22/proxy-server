from dataclasses import dataclass
from decimal import Decimal


@dataclass
class GasInfo:
    id: int
    coords: tuple[Decimal, Decimal]
    number: int
    address: str
    urls: list[str]
    services: list[str]


@dataclass
class FuelInfo:
    name: str
    price: Decimal
    currency: str


@dataclass
class StationFuelInfo:
    id: int
    fuel: FuelInfo
