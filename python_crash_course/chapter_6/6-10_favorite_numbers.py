# 6-10_favorite_numbers.py

favorite_numbers = {
    'wally': [78, 91, 324],
    'jean' : [45, 9],
    'michael': [9, 15, 33],
    'annie': [93, 57, 62],
    'bob' : [26, 179],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t" + str(number).title())
