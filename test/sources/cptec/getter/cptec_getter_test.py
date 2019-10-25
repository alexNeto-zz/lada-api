import unittest

from api.sources.cptec.getter.cptec_getter import CptecGetter


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.__cptec_api_getter = CptecGetter('sp', 'sao-jose-dos-campos')  # São José Dos Campos - SP

    def test_retrieving_data_from_api(self):
        self.assertIsNotNone(self.__cptec_api_getter.make_request())


if __name__ == '__main__':
    unittest.main()
