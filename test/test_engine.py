import unittest

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capulet_engine.need_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 35000
        last_service_mileage = 4000
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet_engine.need_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby_engine.need_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 70000
        last_service_mileage = 5000
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby_engine.need_service())

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(sternman_engine.need_service())

    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternman_engine.need_service())


if __name__ == '__main__':
    unittest.main()
