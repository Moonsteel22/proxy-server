from typing import Generator

from faker import Faker

from integration.logic.schemas import GasInfo, Coordinates, Service
import random

GAS_STATION_EXPONENT = 10000
SERVICES_EXPONENT = 100
LATITUDE_MIN, LATITUDE_MAX = 53, 60
LONGITUDE_MIN, LONGITUDE_MAX = 35, 60


class FirstSource:
    """
    Класс, для получения данных из первого истончика.
    Возвращает фейковые данные
    """

    def __init__(self, fake: Faker):
        self.fake = fake

    def get_data(self) -> Generator[GasInfo, None, None]:
        _urls = [
            "https://www.tatneft.ru/uploads/photos/Frame-5-6172756e81141.png",
            "https://tatneft-info.ru/wp-content/uploads/2021/01/zapravki-tatneft.jpg",
            "https://avatars.mds.yandex.net/get-altay/6195924/2a00000181e79b57d454aa343fa613f5b1f6/XXL_height",
        ]
        _services = [
            Service(f"Service - {i}")
            for i in range(random.randint(1, SERVICES_EXPONENT * 10 - 1))
        ]
        return (
            GasInfo(
                id=i,
                number=i,
                coords=Coordinates(
                    latitude=random.random()
                    + random.randint(LATITUDE_MIN, LATITUDE_MAX),
                    longitude=random.random()
                    + random.randint(LONGITUDE_MIN, LONGITUDE_MAX),
                ),
                address=self.fake.address(),
                urls=_urls,
                services=random.choices(_services, k=3),
            )
            for i in range(
                random.randint(GAS_STATION_EXPONENT, GAS_STATION_EXPONENT * 10 - 1)
            )
        )
