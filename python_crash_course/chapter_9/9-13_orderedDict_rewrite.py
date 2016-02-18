from collections import OrderedDict

glossary = OrderedDict()


glossary['string'] = 'simply a series of characters.'
glossary['list'] = 'is a collection of items in a particular order.'
glossary['append'] = 'is a method that adds an item to the list.'
glossary['tuple'] = 'is an immutable list.'
glossary['dictionary'] = 'is a collection of key-value pairs.'
glossary['items()'] = 'this method returns a list of key-value pairs.'
glossary['sorted()'] = 'function that displays a list in a particular order.'
glossary['values()'] = 'method that return a list of values without any keys.'
glossary['append()'] = 'this method add a new element to the end of a list.'
glossary['reverse()'] = 'reverses the original order of a list permanently.'

for word, meaning in glossary.items():
    print("\n" + word.upper() + ":" +
          "\n\t" + meaning.capitalize())