from abc import ABC
from Battery import Battery

class Splinder(Battery,ABC):

    def __init__(self,current_date,last_service_date):
        self._last_service_date = last_service_date
        self._current_date = current_date

    def need_service(self):
        self._last_service_date = self._last_service_date.replace(self._last_service_date.year + 2)
        if self._last_service_date > self._current_date:
            return True
        else:
            return False