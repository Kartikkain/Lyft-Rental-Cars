import unittest
from engine.Tier.octoprime_tier import Octoprime
from engine.Tier.carrigan_tier import Carrigan


class TestOctoprime(unittest.TestCase):
    def test_tier_should_be_serviced(self):
        tier_pressure = [1, 0.9, 1, 0.5]
        octoprime_tier = Octoprime(tier_pressure)
        self.assertTrue(octoprime_tier.need_service())

    def test_tier_should_not_be_serviced(self):
        tier_pressure = [0.5, 0.9, 0.1, 0.5]
        octoprime_tier = Octoprime(tier_pressure)
        self.assertFalse(octoprime_tier.need_service())


class TestCarrigan(unittest.TestCase):
    def test_tier_should_be_serviced(self):
        tier_pressure = [0.5, 0.6, 0.9, 1]
        carrigan_tier = Carrigan(tier_pressure)
        self.assertTrue(carrigan_tier.need_service())

    def test_tier_should_not_be_serviced(self):
        tier_pressure = [0.5, 0.6, 0.8, 0.2]
        carrigan_tier = Carrigan(tier_pressure)
        self.assertFalse(carrigan_tier.need_service())


if __name__ == '__main__':
    unittest.main()