# Exercise 4-2.py
# This program draws such a archery target.

from graphics import *

def main():
    win = GraphWin("Archery Target", 400, 400)
    win.setBackground("white")
    win.setCoords(0.0, 0.0, 12.0, 12.0)
    shape5 = Circle(Point(6.0, 6.0), 5)
    shape5.setOutline("black")
    shape5.setFill("white")
    shape5.draw(win)
    shape4 = Circle(Point(6.0, 6.0), 4)
    shape4.setFill("black")
    shape4.draw(win)
    shape3 = Circle(Point(6.0, 6.0), 3)
    shape3.setOutline("black")
    shape3.setFill("blue")
    shape3.draw(win)
    shape2 = Circle(Point(6.0, 6.0), 2)
    shape2.setOutline("black")
    shape2.setFill("red")
    shape2.draw(win)
    shape1 = Circle(Point(6.0, 6.0), 1)
    shape1.setOutline("black")
    shape1.setFill("yellow")
    shape1.draw(win)
    p = Point(6.0, 6.0)
    p.draw(win)

    # wait for click and then quit
    win.getMouse()
    win.close()


main()
