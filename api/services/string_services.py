import unidecode


def normalize(string_to_normalize) -> str:
    return unidecode.unidecode(string_to_normalize) if isinstance(string_to_normalize, str) else ""
