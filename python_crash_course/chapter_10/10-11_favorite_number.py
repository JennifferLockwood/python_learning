import json

favorite_number = input("What is your favorite number? ")
filename = 'favorite_number.json'
with open(filename, 'w') as f_obj:
    json.dump(favorite_number, f_obj)
