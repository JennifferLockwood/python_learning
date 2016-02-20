prompt = "Please enter your name to register it in our guest book:"
prompt += "\n(Enter 'quit' to end the program.)"

filename = 'guest_book.txt'
active = True
with open(filename, 'a') as file_object:
    while active:
        message = input(prompt)
        file_object.write(message.title() + " has visited us recently.\n")

        if message == 'quit':
            active = False
        else:
            print("Hello, " + message.title())
            print("You have been registered in our guest book.")
