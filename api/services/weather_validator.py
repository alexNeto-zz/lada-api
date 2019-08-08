def rain_probability(value):
    try:
        result = __validate_rain_probability(value)
    except ValueError:
        result = None
    return result


def __validate_rain_probability(value):
    to_validate = float(value)
    if 0 <= float(to_validate) <= 100:
        return to_validate
    else:
        return None
