# exercise6-3.py
#    A program that calculates the volume and surface area
#    of a sphere from its radius.

import math # Makes the math library available.

def sphereVolume(radius):
    volume = (4 / 3) * math.pi * radius**3
    print("The volume of sphere is: {0:0.4f}".format(volume))

def sphereArea(radius):
    areaSurf = math.pi * 4 * radius**2
    print("The surface area of sphere is: {0:0.4f}".format(areaSurf))

def main():
    print("This program calculates the volume and surface area\n" + \
          "of a sphere from its radius")
    print()
    radius = eval(input("Please enter the radius: "))
    sphereArea(radius)
    sphereVolume(radius)
    print()

main()


