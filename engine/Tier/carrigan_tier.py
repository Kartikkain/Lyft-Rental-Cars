from Tiers import Tires


class Carrigan(Tires):
    def __init__(self, tier_pressure):
        self._tier_pressure = tier_pressure

    def need_service(self):
        for tier in self._tier_pressure:
            if tier >= 0.9:
                return True

        return False
