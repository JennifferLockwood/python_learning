# 4-11_my_list_your_list.py

my_pizzas = ['greek', 'pesto chicken', 'vegetarian', 'traditional']
your_pizzas = my_pizzas[:]

my_pizzas.append('the greek')
your_pizzas.append('stockyard')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print("- " + pizza.title())

print("\nMy friend's favorite pizzas are:")
for pizza in your_pizzas:
    print("- " + pizza.title())
