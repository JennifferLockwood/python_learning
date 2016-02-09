def build_profile(first, last, **user_info):
    '''Build a dictionary containing everything we know about a user.'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('michael', 'jones',
                             location='boston',
                             age= 45, pet= 'cockatiel')
print(user_profile)