# slopeLine
#    A program that calculates the slope of a line.
#    Given the coordinates of the two points.

def main():
    print("This program calculate the slope of a line given the coordinates of the points.")
    print()

    x1, y1 = eval(input("Please enter the coordinates of the first point in the form x,y: "))
    x2, y2 = eval(input("Please enter the coordinates of the second point in the form x,y: "))
    slope = (y2 - y1) / (x2 - x1)
    print()
    print("The slope of the line is:", "{0:0.2f}".format(slope))

main()

