# pizza.py

# Store information about a pizza beind ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summariza the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping.title())
