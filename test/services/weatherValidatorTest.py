import unittest

from api.services.weather_validator import rain_probability, temperature


class MyTestCase(unittest.TestCase):
    def test_rain_probability_negative_integer(self):
        self.assertEqual(None, rain_probability(-1))

    def test_rain_probability_negative_float(self):
        self.assertEqual(None, rain_probability(-1.1))

    def test_rain_probability_negative_string(self):
        self.assertEqual(None, rain_probability('-1'))

    def test_rain_probability_over_100_integer(self):
        self.assertEqual(None, rain_probability(101))

    def test_rain_probability_over_100_float(self):
        self.assertEqual(None, rain_probability(101.1))

    def test_rain_probability_over_100_string(self):
        self.assertEqual(None, rain_probability('101'))

    def test_rain_probability_string_not_digit(self):
        self.assertEqual(None, rain_probability('aaaaaa1212'))

    def test_rain_probability_in_interval_integer(self):
        self.assertEqual(12, rain_probability(12))

    def test_rain_probability_in_interval_float(self):
        self.assertEqual(12.34, rain_probability(12.34))

    def test_rain_probability_in_interval_string(self):
        self.assertEqual('54.121', rain_probability('54.121'))

    def test_temperature(self):
        self.assertEqual("12", temperature("12"))


if __name__ == '__main__':
    unittest.main()
