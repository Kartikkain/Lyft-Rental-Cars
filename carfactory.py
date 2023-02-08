from abc import ABC
from car import Car
class CarFactory(Car,ABC):
    def __init__(self,engine,battery):
        super().__init__(engine,battery)

    def create_calliope(self):
        return super().need_service()
    def create_glissade(self):
        return super().need_service()
    def create_palindrome(self):
        return super().need_service()
    def create_rorschach(self):
        return super().need_service()
    def create_thovex(self):
        return super().need_service()