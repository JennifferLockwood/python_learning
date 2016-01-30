# conditional_tests.py

requested_sauce = ['zesty red', 'creamy garlic', 'polynesian', 'bbq']

print("Our available sauces are:")
for sauce in requested_sauce:
    if sauce == 'bbq':
        print("- " + sauce.upper())
    else:
        print("- " + sauce.title())
        
topping = 'black olives'
if topping == 'black olives':
    print("\nAdd " + topping + " to this pizza")
if topping != 'mushrooms':
    print("Hold the mushrooms!")

car = 'Hyundai'
if car.lower() == 'hyundai':
    print("\nIt's not right to write " + car.lower())
print("It's right to write a car brand like this: " + car + ".\n")
