def make_sandwich(*veggies):
    '''Summarize the pizza we are about to make.'''
    print("\nMaking a sandwich with the following veggies:")
    for vegetable in veggies:
        print("- " + vegetable.capitalize())

make_sandwich('spinach', 'cucumbers', 'olives', 'avocado')
make_sandwich('lettuce', 'onion', 'tomato', 'green peppers')
