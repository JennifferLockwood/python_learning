# 6-4_glosary_2.py

glosary = {
    'string': 'simply a series of characters.',
    'list': 'is a collection of items in a particular order.',
    'append': 'is a method that adds an item to the list.',
    'tuple': 'is an immutable list.',
    'dictionary': 'is a collection of key-value pairs.',
    'items()': 'this method returns a list of key-value pairs.',
    'sorted()': 'function that displays a list in a particular order.',
    'values()': 'method that return a list of values without any keys.',
    'append()': 'this method add a new element to the end of a list.',
    'reverse()': 'reverses the original order of a list permanently.',
    }

for word, meaning in glosary.items():
    print("\n" + word.upper() + ":" +
          "\n\t" + meaning.capitalize())
