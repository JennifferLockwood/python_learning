# sphere.py
#    A program that calculates the volume and surface area
#    of a sphere from its radius.

import math # Makes the math library available.

def main():
    print("This program calculates the volume and surface area of a sphere from its radius")
    print()

    radius = eval(input("Please enter the radius: "))
    volume = (4 / 3) * math.pi * radius**3
    areaSurf = math.pi * 4 * radius**2

    print()
    print("The volume of sphere is: ", volume)
    print("The surface area of sphere is: ", areaSurf)

main()


