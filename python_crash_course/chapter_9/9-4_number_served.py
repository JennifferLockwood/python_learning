class Restaurant():
    '''A simple attempt to model a restaurant.'''

    def __init__(self, name, cuisine_type):
        '''Initialize name and cuisine_type attributtes.'''
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''Simulate naming the restaurante.'''
        print("Restaurant " + self.name.title() + ", " +
              self.cuisine_type.title() + " cuisine.")

    def open_restaurant(self):
        print("Restaurant " + self.name.title() + " is open!")

    def customers_served(self):
        '''Print a statement showing number of customers served.'''
        print("The restaurant has served " + str(self.number_served) +
              " customers today.")

    def set_number_served(self, number):
        '''
        Set the number of customers that have been served.
        Reject the change if it attempts to do negative increments.
        '''
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You can't do negative increments!")

    def increment_number_served(self,customers):
        '''Add the number of customers who have been served.'''
        self.number_served += customers

my_restaurant = Restaurant('the visconti', 'italian')
print("My favorite restaurant is " + my_restaurant.name.title() + ".")
print("My favorite restaurant has " + my_restaurant.cuisine_type +
      " food.")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.set_number_served(34)
my_restaurant.customers_served()

my_restaurant.increment_number_served(18)
my_restaurant.customers_served()