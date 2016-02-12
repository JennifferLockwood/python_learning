class User():
    '''A simple attempt to describe users.'''

    def __init__(self, first_name, last_name, occupation, country, city,):
        '''Initialize first_name and last_name attributtes.'''
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.country = country
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        '''Simulate user's full name and occupation.'''
        full_name = self.first_name + " " + self.last_name
        print(full_name.title() + " lives in " + self.country.title() + ".")

    def greeter_user(self):
        '''Simulate a greeting.'''
        print("Hello " + self.first_name.title() +
              ", welcome to our website!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

my_user = User('michael', 'clooney', 'carpenter', 'france', 'lyon')
your_user = User('anna', 'williams', 'nurse', 'canada', 'quebec')
his_user = User('carlos','robin', 'student', 'china', 'pekin')

my_user.describe_user()
my_user.greeter_user()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
print("You have tried to login " + str(my_user.login_attempts) + " times.")
my_user.reset_login_attempts()
print("You have " + str(my_user.login_attempts) + " attempts left.\n")