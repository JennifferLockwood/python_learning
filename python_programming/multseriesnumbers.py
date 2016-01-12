# multseriesnumbers.py
#    A program that computes the multiplication of a series of numbers
#    Entered by the user.

def main():
    total = 1
    n = eval(input("Please enter how many numbers are to be multiplied: "))

    for i in range(n):
        number = eval(input("Please enter a number: "))
        total = number * total

    print("The product of the multiplication of the series of numbers is: ", total)

main()

