import unidecode


def normalize(string_to_normalize):
    return unidecode.unidecode(string_to_normalize) if type(string_to_normalize) is str else ""
