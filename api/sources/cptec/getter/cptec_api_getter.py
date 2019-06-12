import requests
from bs4 import BeautifulSoup


class CptecAPIGetter:

    def __init__(self, latitude, longitude):
        self.__url = 'http://servicos.cptec.inpe.br/XML/cidade/7dias/{0}/{1}/previsaoLatLon.xml'
        self.__response = ''
        self.__parsed_response = ''
        self.__latitude = latitude
        self.__longitude = longitude

    def __get_data_from_request(self):
        self.__response = requests.get(self.__url.format(self.__latitude, self.__longitude)).content
        return self

    def __html_parser(self):
        self.__parsed_response = BeautifulSoup(self.__response, 'xml')
        return self

    def make_request(self):
        self.__get_data_from_request().__html_parser()
        return self.__parsed_response
