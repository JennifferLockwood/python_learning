def show_magicians(magicians):
    '''Print a simple list of magician's names.'''
    for name in magicians:
        msg = name.title() + ", that's a great trick!"
        print(msg)

magicians = ['david', 'harry', 'criss', 'paul']
show_magicians(magicians)