import unittest

from api.services.brazil_region_parser import get_abb_of


class MyTestCase(unittest.TestCase):
    def test_region_with_space(self):
        self.assertEqual('sp', get_abb_of('São Paulo'))

    def test_region_with_invalid_name(self):
        self.assertEqual('', get_abb_of('Inválido'))

    def test_region_with_number(self):
        self.assertEqual('', get_abb_of('19291'))


if __name__ == '__main__':
    unittest.main()
