class User:
    """A simple attempt to describe users."""

    def __init__(self, first_name, last_name, occupation, country, city):
        """Initialize first_name and last_name attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.country = country
        self.city = city

    def describe_user(self):
        """Simulate user's full name and occupation."""
        full_name = self.first_name + " " + self.last_name
        print(full_name.title() + " lives in " + self.country.title() + ".")

    def greeter_user(self):
        """Simulate a greeting."""
        print("Hello " + self.first_name.title() +
              ", welcome to our website!")