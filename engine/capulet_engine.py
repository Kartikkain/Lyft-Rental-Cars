from abc import ABC
from Engines import Engine


class CapuletEngine(Engine, ABC):
    def __init__(self, current_mileage, last_service_mileage):
        self._current_mileage = current_mileage
        self._last_service_mileage = last_service_mileage

    def need_service(self):
        return self._current_mileage - self._last_service_mileage > 30000
