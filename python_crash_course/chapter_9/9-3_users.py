class User():
    """A simple attempt to describe users."""

    def __init__(self, first_name, last_name, occupation, country, city,):
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

my_user = User('michael', 'clooney', 'carpenter', 'france', 'lyon')
your_user = User('anna', 'williams', 'nurse', 'canada', 'quebec')
his_user = User('carlos','robin', 'student', 'china', 'pekin')

my_user.describe_user()
my_user.greeter_user()
print(my_user.first_name.title() + " is a " + my_user.occupation +
" who lives in " + my_user.city.title() + ", " + my_user.country.title() +
".\n")

your_user.describe_user()
your_user.greeter_user()
print(your_user.first_name.title() + " is a " + your_user.occupation +
" who lives in " + your_user.city.title() + ", " + your_user.country.title() +
".\n")

his_user.describe_user()
his_user.greeter_user()
print(his_user.first_name.title() + " is a " + his_user.occupation +
" who lives in " + his_user.city.title() + ", " + his_user.country.title() +
".\n")