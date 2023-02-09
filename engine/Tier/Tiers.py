from abc import ABC, abstractmethod


class Tires(ABC):

    @abstractmethod
    def need_service(self):
        pass