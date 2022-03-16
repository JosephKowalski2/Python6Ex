import unittest

import temperature_utils_v2


class TemperatureUtilsV2Test(unittest.TestCase):

    def test_convert_to_kelvin_from_celsuis(self):
        test_cases = [
            (32, 305.15),
            (68, 341.15),
            (100, 373.15),
            (20.2, 293.35)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_to_kelvin_from_celsuis(temp_in))


    def test_convert_to_kelvin_from_fahrenheit(self):
        test_cases = [
            (32, 273.15),
            (68, 293.15),
            (100, 310.93),
            (20.2, 266.59)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_to_kelvin_from_fahrenheit(temp_in))
