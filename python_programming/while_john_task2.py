# while_john_task.py

def your_number():
    num = eval(input("Enter a natural number less than 100: "))
    idhai = 0
    while num > 0:
        print("You entered: ", num)
        idahi = idahi + 1
    else:
        print("Try again and enter a number.")        

def main():
    your_number()

main()
