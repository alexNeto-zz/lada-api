from api.services.string_services import normalize

statesDict = {
    'acre': 'ac',
    'alagoas': 'al',
    'amapa': 'ap',
    'amazonas': 'am',
    'bahia': 'ba',
    'ceara': 'ce',
    'distrito federal': 'df',
    'espirito santo': 'es',
    'goias': 'go',
    'maranhao': 'ma',
    'mato grosso': 'mt',
    'mato grosso so sul': 'ms',
    'minas gerais': 'mg',
    'para': 'pa',
    'paraiba': 'pb',
    'parana': 'pr',
    'pernambuco': 'pe',
    'piaui': 'pi',
    'rio de janeiro': 'rj',
    'rio grande do norte': 'rn',
    'rio grande do sul': 'rs',
    'rondonia': 'ro',
    'roraima': 'rr',
    'santa catarina': 'sc',
    'sao paulo': 'sp',
    'sergipe': 'se',
    'tocantins': 'to'
}


def get_abb_of(region: str) -> str:
    normalized_region = normalize(region.lower())
    if normalized_region in statesDict:
        return statesDict[normalized_region]
    else:
        return ''
