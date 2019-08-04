import unittest

from api.sources.cptec.getter.cptec_api_getter import CptecAPIGetter


class CptecAPIGetterTest(unittest.TestCase):
    def setUp(self):
        self.__cptec_api_getter = CptecAPIGetter(-22.87216997446473, -48.44871995614285)  # Botucatu - SP

    def test_retrieving_data_from_api(self):
        self.assertIsNotNone(self.__cptec_api_getter.make_request())


if __name__ == '__main__':
    unittest.main()
