def make_shirt(size='large', printed_message='i love python'):
    '''Display the size of a shirt and the message print on it.'''
    print("\nThis t-shirt is size " + size + ".")
    print('Message print on it: ' + printed_message.title())

make_shirt()
make_shirt(size='medium')
make_shirt(size='Xlarge', printed_message='johnsin pensando...')
