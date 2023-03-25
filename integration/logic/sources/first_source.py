from proxy_server.integration.logic.schemas import GasInfo


class FirstSource:
    def get_data(self) -> GasInfo:
        ...
