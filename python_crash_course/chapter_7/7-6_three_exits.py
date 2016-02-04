prompt = "\nWhat toppings do you want for your pizza today?"
prompt += "\nEnter 'quit' to end your toppings. "

'''
while True:
    message = input(prompt)

    if message == 'quit':
        # break
    else:
        print("You'll add " + message + " to your pizza.")

print("You finished your order.")
'''

message = ""
while message != 'quit':
    message = input(prompt)
    print("You'll add " + message + " to your pizza.")

    if message != 'quit':
        print(message)