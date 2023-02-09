from Tiers import Tires


class Octoprime(Tires):
    def __init__(self, tire_pressure):
        self._tire_pressure = tire_pressure
        self._sum = 0

    def need_service(self):
        for tier in self._tire_pressure:
            self._sum += tier

        return self._sum >= 3

