def city_country(city, country, population=''):
    """TIY 11-1. Return city-country pairs, neatly formatted."""
    if population:
        city_country_pair = city.capitalize() + ', ' + country.capitalize()
        city_country_pair += ' - population ' + population
    else:
        city_country_pair = city.capitalize() + ', ' + country.capitalize()
    return city_country_pair
