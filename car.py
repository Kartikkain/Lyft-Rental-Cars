from abc import ABC
from Service import Service

class Car(Service,ABC):
    def __init__(self, engine,battery):
        self._engine = engine
        self._battery = battery

    def need_service(self):
        if self._engine.need_service() or self._battery.need_service() :
            return True
        else:
            return False
