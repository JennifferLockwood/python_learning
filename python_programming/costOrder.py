# costOrder
#    A program that calculates the total cost of an order of coffee.

def main():
    print("This program calculate the total cost of an order of a given number of pounds coffee")
    print()

    pounds = eval(input("How many pounds of coffee do you want? "))
    total = (pounds * (10.50 + 0.86)) + 1.50
    print()
    print("The total cost of your order is $", "{0:0.2f}".format(total))

main()

