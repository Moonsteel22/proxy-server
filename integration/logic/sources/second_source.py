from proxy_server.integration.logic.schemas import StationFuelInfo


class SecondSource:
    def get_data(self) -> StationFuelInfo:
        ...
