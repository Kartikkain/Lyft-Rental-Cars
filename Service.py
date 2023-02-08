from abc import ABC,abstractmethod

class Service(ABC):

    @abstractmethod
    def need_service(self):
        pass
    