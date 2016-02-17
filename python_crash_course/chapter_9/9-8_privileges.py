class User():
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

class Privileges():
    """A simple attempt to model privileges for a user."""

    def __init__(self):
        """Initialize the privileges' attributes."""
        privileges = ['can add a post', 'can delete a post',
                           'can ban user', 'can change security settings']
        self.privileges = privileges

    def describe_privileges(self):
        """Print a statement describing the privileges."""
        print("This person has the following privileges:")

        for privilege in self.privileges:
            print("- " + privilege.capitalize())


class Admin(User):
    """Represents aspects of a special king of user, an administrator."""
    def __init__(self, first_name, last_name, occupation, country, city):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an administrator.
        """
        super().__init__(first_name, last_name, occupation, country, city)
        self.list_privileges = Privileges()
            

admin_user = Admin('michael', 'clooney', 'administrator', 'canada', 'quebec')
admin_user.describe_user()
admin_user.greeter_user()
admin_user.list_privileges.describe_privileges()