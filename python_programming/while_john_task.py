# while_john_task.py

def your_number(num):
    while num < 100:
        print("You entered: ", num)
    else:
        print("Try again and enter a number.")        

def main():
    number = eval(input("Enter a natural number less than 100: "))
    your_number(number)

main()
