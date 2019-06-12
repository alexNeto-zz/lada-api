import requests
from bs4 import BeautifulSoup


class CptecGetter:

    def __init__(self, state, city):
        self.__url = 'https://www.cptec.inpe.br/previsao-tempo'  # sp/sao-jose-dos-campos
        self.__response = ''
        self.__parsed_response = ''
        self.__state = state
        self.__city = city

    def __get_data_from_request(self):
        self.__response = requests.get("{0}/{1}/{2}".format(self.__url, self.__state, self.__city)).content
        return self

    def __html_parser(self):
        self.__parsed_response = BeautifulSoup(self.__response, 'html.parser')
        return self

    def make_request(self):
        self.__get_data_from_request().__html_parser()
        return self.__parsed_response
