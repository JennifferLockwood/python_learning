# exercise6-5.py

import math

def areaPizza(diameter):
    totalArea = math.pi * (diameter / 2)**2
    print("The total area of the pizza is {0:0.2f} inches.".format(totalArea))

def inchCost(diameter, price):
    squareInchCost = price / (math.pi * (diameter / 2)**2)
    print("The cost per square inch of the circular pizza is ${0:0.2f}.".format(squareInchCost))

def main():
    print("This program calculates the cost per square inch")
    print("of the circular pizza.")

    diameter, price = eval(input("Please enter the diameter and price of" +
                                 " the pizza separeated by a comma: "))
    areaPizza(diameter)
    inchCost(diameter, price)
    print()

main()
    
