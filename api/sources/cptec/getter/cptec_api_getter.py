import requests
from bs4 import BeautifulSoup


class CptecAPIGetter:

    def __init__(self, x, y):
        self.__url = 'http://servicos.cptec.inpe.br/XML/cidade/7dias/{0}/{1}/previsaoLatLon.xml'
        self.__response = ''
        self.__parsed_response = ''
        self.x = x
        self.y = y

    def __get_data_from_request(self):
        self.__response = requests.get(self.__url.format(self.x, self.y)).content
        return self

    def __html_parser(self):
        self.__parsed_response = BeautifulSoup(self.__response, 'xml')
        return self

    def make_request(self):
        self.__get_data_from_request().__html_parser()
        return self.__parsed_response
