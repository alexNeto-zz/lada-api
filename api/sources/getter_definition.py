import requests
from bs4 import BeautifulSoup


class GetterDefinition:
    def __init__(self, config: dict, arg0: str, arg1: str):
        self.__url = config['url']
        self.__response = ''
        self.__parser = config['parser']
        self.__parsed_response = ''
        self.__arg0 = arg0
        self.__arg1 = arg1

    def __get_data_from_request(self):
        if self.__parser != 'json':
            self.__response = requests.get(self.__url.format(self.__arg0, self.__arg1)).content
        else:
            self.__response = requests.get(self.__url.format(self.__arg0, self.__arg1)).json()
        return self

    def __parse(self):
        self.__parsed_response = BeautifulSoup(self.__response, self.__parser)
        return self

    def make_request(self):
        if self.__parser != 'json':
            self.__get_data_from_request().__parse()
            return self.__parsed_response
        else:
            self.__get_data_from_request()
            return self.__response
