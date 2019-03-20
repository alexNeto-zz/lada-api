from pymongo import MongoClient

from services.singleton import singleton


@singleton
class Storage:

    def __init__(self):
        self.__connection = None
        self.__database = "lada"

    def make_connection(self):
        if self.__connection is None:
            self.__connection = MongoClient('localhost', 27017)

    def conn(self):
        return self.__connection[self.__database]
