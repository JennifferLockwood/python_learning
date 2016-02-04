prompt = "\nWhat is your age?"
prompt += "\nEnter number 0 to end the program. "

active = True
while active:
    age = input(prompt)
    age = int(age)
    
    if age == 0:
        active = False

    elif age < 3:
        print("The cost of your movie ticket is free!")
    elif age <= 12:
        print("The cost of your movie ticket is $10.")

    else:
        print("The cost of your movie ticket is $12.")
