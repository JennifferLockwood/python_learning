# lengthladder.py
#    A program that calculates the length of a ladder given height and angle
#    of a ladder.

import math # Makes the math library available.

def main():
    print("This program calculates the length of a ladder given height and angle.")
    print()

    degrees = eval(input("Please enter the angle of the ladder in degrees: "))
    height = eval(input("Please enter the height of the ladder: "))
    length = height / (math.sin((math.pi / 180) * degrees))
    print()
    
    print("The length of a ladder required to reach is:", "{0:0.2f}".format(length))

main()

