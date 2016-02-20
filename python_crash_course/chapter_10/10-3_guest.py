filename = 'guest.txt'

name = input("Please, enter your full name: ")
with open(filename, 'w') as file_object:
    file_object.write(name)