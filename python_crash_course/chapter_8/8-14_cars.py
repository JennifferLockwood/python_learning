def build_info(make, model, **car_info):
    '''Build a dictionary containing everything we know about a user.'''
    information = {}
    information['manufacturer'] = make
    information['model_name'] = model
    for key, value in car_info.items():
        information[key] = value
    return information

car_profile = build_info('toyota', 'tacoma',
                         color='gray', mileage=45000,
                         year=2010)
print(car_profile)