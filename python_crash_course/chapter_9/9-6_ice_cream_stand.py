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

class IceCreamStand(Restaurant):
    '''Represents a specific kind of restaurant, ice cream stand.'''

    def __init__(self, name, cuisine_type):
        '''
        Initialize attributes of the parent class.
        Then initialize attributtes specific to an ice cream stand.
        '''
        super().__init__(name,cuisine_type)
        self.flavors = ['vanilla', 'coffee', 'dark chocolate', 'strawberry']

    def list_flavors(self):
        '''Print a list of flavors.'''
        print("This is their selection of flavors:")

        for flavor in self.flavors:
            print("- " + flavor.capitalize())


my_cold_stone = IceCreamStand('cold stone', 'creamery')
print("My favorite dessert place is " + my_cold_stone.name.title() + ".")
print("My favorite dessert place is a " + my_cold_stone.cuisine_type + ".")
my_cold_stone.list_flavors()
my_cold_stone.open_restaurant()