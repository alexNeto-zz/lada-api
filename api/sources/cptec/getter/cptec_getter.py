from api.sources.getter_definition import GetterDefinition


class CptecGetter(GetterDefinition):
    def __init__(self, state, city):
        config = {
            'url': 'https://www.cptec.inpe.br/previsao-tempo/{0}/{1}',
            'parser': 'html.parser'
        }
        GetterDefinition.__init__(self, config, state, city)
