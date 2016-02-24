import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def get_and_greet_new_user():
    username = get_new_username()
    print("We'll remember you when you come back, " + username + "!")


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        correct_username = input("Is " + username + " your correct username? (Y/n) ")
        if correct_username == 'n':
            get_and_greet_new_user()
        else:
            print("Welcome back, " + username + "!")
    else:
        get_and_greet_new_user()

greet_user()
