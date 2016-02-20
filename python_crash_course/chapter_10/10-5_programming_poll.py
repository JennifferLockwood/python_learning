prompt = "Please let's us know why you like programming:"
prompt += "\n(Enter 'quit' to end the program.) "

filename = 'programming_poll_responses.txt'
active = True
with open(filename, 'a') as file_object:
    while active:
        message = input(prompt)
        file_object.write(message.capitalize() + ".\n")

        if message == 'quit':
            active = False
        else:
            print("Thank you for responding our poll.")