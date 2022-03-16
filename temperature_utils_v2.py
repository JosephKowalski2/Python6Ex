def convert_to_kelvin_from_celsuis(temperature):
    return round(temperature + 273.15, 2)


def convert_to_kelvin_from_fahrenheit(temperature):
    return round((temperature - 32) * (5 / 9) + 273.15, 2)

