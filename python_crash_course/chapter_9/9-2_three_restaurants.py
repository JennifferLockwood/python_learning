class Restaurant():
    '''A simple attempt to model a restaurant.'''

    def __init__(self, name, cuisine_type):
        '''Initialize name and cuisine_type attributtes.'''
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''Simulate naming the restaurante.'''
        print("Restaurant " + self.name.title() + ", " +
              self.cuisine_type.title() + " cuisine.")

    def open_restaurant(self):
        print("Restaurant " + self.name.title() + " is open!")

my_restaurant = Restaurant('the visconti', 'italian')
your_restaurant = Restaurant('macarroni grill', 'italian')
bob_restaurant = Restaurant('el pollo loco', 'mexican')

my_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
bob_restaurant.describe_restaurant()