def temperature(value):
    return try_or_none(lambda: __validate_value(value, -100))


def rain_probability(value):
    return try_or_none(lambda: __validate_value(value) / 100)


def __validate_value(value, minimum=0, maximum=100):
    to_validate = float(value)
    if minimum <= float(to_validate) <= maximum:
        return to_validate
    else:
        return 0


def try_or_none(on_try):
    try:
        return on_try()
    except ValueError:
        return 0
