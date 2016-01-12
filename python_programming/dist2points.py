# dist2points
#    A program that calculates the distance between two points.
#    Given the coordinates of the two points.

import math # Makes the math library available.

def main():
    print("This program calculate the distance between two poins given their coordinates.")
    print()

    x1, y1 = eval(input("Please enter the coordinates of the first point in the form x,y: "))
    x2, y2 = eval(input("Please enter the coordinates of the second point in the form x,y: "))
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print()
    
    print("The distance between the points is:", "{0:0.4f}".format(distance))

main()

