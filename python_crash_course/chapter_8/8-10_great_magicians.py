def show_magicians(magicians):
    '''Print a simple list of magician's names.'''
    for name in magicians:
        print("- "  + name.title())

def make_great(magicians_names, great_magicians):
    '''
    Modify the list of magicians by adding the phrase
    the Great to each magician's name.
    '''
    while magicians_names:
        current_magician = 'the great ' + magicians_names.pop()
        great_magicians.append(current_magician)

magicians = ['david', 'harry', 'criss', 'paul']
great_magicians = []

make_great(magicians, great_magicians)
show_magicians(great_magicians)
show_magicians(magicians)
