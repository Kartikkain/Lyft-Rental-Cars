from abc import ABC
from car import Car
class CarFactory(Car,ABC):
    def __init__(self,engine,battery):
        super().__init__(engine,battery)
