import unittest
from datetime import datetime
from engine.Battery.nubbin_battery import Nubbin
from engine.Battery.splinder_battery import Splinder


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        last_service_date = last_service_date.replace(year=last_service_date.year - 3)
        nubbin_battery = Nubbin(current_date, last_service_date)
        self.assertTrue(nubbin_battery.need_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        last_service_date = last_service_date.replace(year=last_service_date.year - 1)
        nubbin_battery = Nubbin(current_date, last_service_date)
        self.assertFalse(nubbin_battery.need_service())


class TestSplinderBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        last_service_date = last_service_date.replace(year=last_service_date.year - 7)
        splinder_battery = Splinder(current_date, last_service_date)
        self.assertTrue(splinder_battery.need_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        last_service_date = last_service_date.replace(year=last_service_date.year - 2)
        splinder_battery = Splinder(current_date, last_service_date)
        self.assertFalse(splinder_battery.need_service())


if __name__ == '__main__':
    unittest.main()