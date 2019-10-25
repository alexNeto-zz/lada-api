import unittest

from api.services.string_services import normalize, dash, to_key


class StringServiceTest(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual('Sao Paulo', normalize('São Paulo'))

    def test_normalize_None(self):
        self.assertEqual('', normalize(None))

    def test_normalize_empty_string(self):
        self.assertEqual('', normalize(''))

    def test_dash(self):
        self.assertEqual('sao-paulo:sao-jose-dos-campos', dash('São Paulo:São José dos Campos'))

    def test_dash_None(self):
        self.assertEqual('', dash(None))

    def test_dash_empty_string(self):
        self.assertEqual('', dash(''))

    def test_to_key(self):
        self.assertEqual('sao-paulo:sao-jose-dos-campos', to_key('São Paulo', 'São José dos Campos'))

    def test_to_key_None(self):
        self.assertEqual(':', to_key(None, None))

    def test_to_key_empty_string(self):
        self.assertEqual(':', to_key('', ''))


if __name__ == '__main__':
    unittest.main()
