from api.sources.getter_definition import GetterDefinition


class CptecAPIGetter(GetterDefinition):

    def __init__(self, latitude, longitude):
        config = {
            'url': 'http://servicos.cptec.inpe.br/XML/cidade/7dias/{0}/{1}/previsaoLatLon.xml',
            'parser': 'xml'
        }
        GetterDefinition.__init__(self, config, latitude, longitude)
