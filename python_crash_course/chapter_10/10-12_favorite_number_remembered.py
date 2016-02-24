import json

# Load the favorite number, if it has been stored previously.
# Otherwise, prompt for the favorite number and store it.

filename = 'favorite_number.json'
try:
    with open(filename) as f_obj:
        favorite_number = json.load(f_obj)
except FileNotFoundError:
    favorite_number = input("What is your favorite number? ")
    with open(filename, 'w') as f_obj:
        json.dump(favorite_number, f_obj)
        print("We'll remember that " + favorite_number +
              " is yout favorite number when you come back.")
else:
    print("Your favorite number is " + favorite_number + "!")
