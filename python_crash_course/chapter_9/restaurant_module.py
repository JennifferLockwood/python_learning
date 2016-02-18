"""A class that can be used to represent a restaurant."""

class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine_type attributes."""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Simulate naming the restaurante."""
        print("Restaurant " + self.name.title() + ", " +
              self.cuisine_type.title() + " cuisine.")

    def open_restaurant(self):
        print("Restaurant " + self.name.title() + " is open!")