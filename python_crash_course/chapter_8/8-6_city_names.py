def city_country(city, country):
    '''Return city-country pairs, neatly formatted.'''
    city_country_pair = city + ", " + country
    return city_country_pair.title()

print(city_country('santiago', 'chile'))
print(city_country('paris', 'france'))
print(city_country('london', 'england'))