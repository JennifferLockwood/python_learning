# avgseriesnumb.py
#    A program that calculates the average of a series of numbers
#    Entered by the user.

def main():
    total = 0
    n = eval(input("Please enter how many numbers there are: "))

    for i in range(n):
        number = eval(input("Please enter a number: "))
        total = number + total
        result = total / n

    print("The average of the series of numbers is:", float(result))

main()

