# exercise6-6-1.py
import math
from graphics import *

def square(x):
    return x * x

def distance(p1, p2):
    dist = math.sqrt(square(p1.getX() - p2.getX())
                     + square(p1.getY() - p2.getY()))
    return dist

def perimeter(message, p1, p2, p3):
    perim = distance(p1, p2) + distance(p2, p3) + distance(p3, p1)
    message.setText("The perimeter is: {0:0.2f}".format(perim))

def area(message1, perimeter, p1, p2, p3):
    s = perimeter / 2
    area = math.sqrt(s * (s - distance(p1, p2)) * (s - distance(p2, p3)) * (s - distance(p3, p1)))
    message1.setText("The area is: {0:0.2f}".format(areaTriangle))
    

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message1 = Text(Point(5, 9.5), " ")
    message.draw(win)
    message1.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Calculate the perimeter of the triangle
    perimeter(message, p1, p2, p3)

    # Calculate the area of the triangle
    area(message1, perim, p1, p2, p3)

    # Wait for another click to exit
    win.getMouse()
    win.close()
    

main()
