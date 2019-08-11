import unidecode


def normalize(string_to_normalize: str) -> str:
    if isinstance(string_to_normalize, str):
        return unidecode.unidecode(string_to_normalize)
    else:
        return ""


def dash(to_dash: str) -> str:
    return normalize(to_dash).replace(' ', '-').lower()


def to_key(region: str, city: str) -> str:
    return "{0}:{1}".format(dash(region), dash(city))
