# multsumseriesnumbers.py
#    A program that calculates the multiplication and sum of a series
#    Of numbers entered by the user.

def main():
    result = 0
    product = 1
    n = eval(input("Please enter how many numbers are to be summed and multiplied: "))

    for i in range(n):
        number = eval(input("Please enter a number: "))
        result = number + result
        product = number * product

    print("The result of the sum of the series of numbers is", result)
    print("The product of the multiplication of the series of numbers is", product)

main()

