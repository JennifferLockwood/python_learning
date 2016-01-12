# circularPizza
#    A program that calculates the cost per square inch of the circular pizza.
#    Given its diameter and price

import math # Makes the math library available.

def main():
    print("This program calculates the cost per square inch")
    print("of the circular pizza.")

    diameter, price = eval(input("Please enter the diameter and price of the pizza separeated by a comma: "))
    squareInchCost = price / (math.pi * (diameter / 2)**2)

    print()
    print("The cost per square inch of the circular pizza is: ", squareInchCost)

main()
    
