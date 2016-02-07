def describe_city(city_name, country='france'):
    print("\n" + city_name.title() + " is in " + country.title() + ".")

describe_city('paris')
describe_city(city_name='lyon')
describe_city('reykjavik', 'iceland')
describe_city(country='spain', city_name='madrid')
