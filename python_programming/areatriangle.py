# areatriangle.py
#    A program that calculates the area of a triangle given the length of
#    its three side a, b, and c.

import math # Makes the math library available.

def main():
    print("This program calculates the area of a triangle given the length of its sides.")
    print()

    a, b, c = eval(input("Please enter the length of the three sides of a triangle separated by a comma: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print()
    
    print("The area of the triangle is:", "{0:0.2f}".format(area))

main()

