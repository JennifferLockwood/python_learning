from python_crash_course.chapter_9.user_module import User


class Privileges:
    """A simple attempt to model privileges for a user."""

    def __init__(self, privileges):
        """Initialize the privileges' attributes."""
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

        privileges = ['can add a post', 'can delete a post',
                      'can ban user', 'can change security settings']
        self.privileges = Privileges(privileges)