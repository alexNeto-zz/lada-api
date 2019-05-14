import requests
from bs4 import BeautifulSoup


class CptecAPIGetter:

    def __init__(self, state, city):
        self.__url = 'http://servicos.cptec.inpe.br/XML/cidade/7dias/{0}/previsao.xml'
        self.__countries = ['br']
        self.__response = ''
        self.__parsed_response = ''
        self.state = state
        self.city = city

    def __get_data_from_request(self):
        self.__response = requests.get(self.__url.format(self.__find_city())).content
        return self

    def __html_parser(self):
        self.__parsed_response = BeautifulSoup(self.__response, 'xml')
        return self

    def make_request(self):
        self.__get_data_from_request().__html_parser()
        return self.__parsed_response

    def __find_city(self):
        return '244'
