prompt = "\nWhat toppings do you want for your pizza today?"
prompt += "\nEnter 'quit' to end your toppings. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print("You'll add " + message + " to your pizza.")

print("You finished your pizza order.")