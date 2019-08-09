class CptecAPIScrapy:

    def __init__(self, parsed_data):
        self.__data = parsed_data

    def get_updated_at(self):
        return self.__data.find('atualizacao').text

    def get_week_resume(self):
        return list(map(self.__get_day_from_week, self.__data.find_all('previsao')))

    @staticmethod
    def __get_day_from_week(day):
        return {
            "day": day.find('dia').text,
            "weather": day.find('tempo').text,
            "maximum": day.find('maxima').text,
            "minimum": day.find('minima').text,
            "iuv": day.find('iuv').text
        }
