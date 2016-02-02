# 6-11_cities.py

cities = {
    'amsterdam': {
        'country': 'netherlands',
        'population': 814000,
        'fact': 'The largest city and national capital of the Netherlands.',
        },
    'baltimore': {
        'country': 'united states of america',
        'population': 622000,
        'fact': 'The largest city in Maryland, USA.',
        },
    'dublin': {
        'country': 'ireland',
        'population': 528000,
        'fact': 'It is the capital and largest city of Ireland.',
        },
    'helsinki': {
        'country': 'finland',
        'population': 599700,
        'fact': 'The largest city of Finland.',
        },
    }

for city, city_info in cities.items():
    print("\nCITY: " + city.upper())
    print("\tCountry: " + city_info['country'].title())
    print("\tPopulation: " + str(city_info['population']))
    print("\tOne Fact: " + city_info['fact'])
