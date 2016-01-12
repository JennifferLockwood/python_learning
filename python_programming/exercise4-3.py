# exercise4-3.py
# This program draws some sort of a face

from graphics import *

def main():
    win = GraphWin("Sort of a Face", 400, 400)
    win.setBackground("white")
    win.setCoords(0.0, 0.0, 12.0, 12.0)
    shape1 = Circle(Point(6.0, 6.0), 5)
    shape1.setOutline("black")
    shape1.setFill("peachpuff")
    shape1.draw(win)
    nose = Oval(Point(5.0, 5.0), Point(7.0, 6.0))
    nose.setFill("lightsalmon")
    nose.draw(win)
    leftEye = Circle(Point(4.0,8.0), 1.0)
    insideLeftEye = Circle(Point(3.5,8.0), 0.5)
    leftEye.setOutline("black")
    leftEye.setFill("white")
    insideLeftEye.setOutline("black")
    insideLeftEye.setFill("blue")
    rightEye = leftEye.clone() # rightEye is an exact copy of the leftEye
    rightEye.move(4, 0)
    insideRightEye = insideLeftEye.clone()
    insideRightEye.move(4, 0)
    leftEye.draw(win)
    rightEye.draw(win)
    insideLeftEye.draw(win)
    insideRightEye.draw(win)
    lipUp = Rectangle(Point(4.0, 3.0), Point(8.0, 3.5))
    lipUp.setOutline("red")
    lipUp.setFill("darkred")
    lipDown = lipUp.clone()      # lipDown is an exact copy of the lipUp
    lipDown.move(0, -0.5)
    lipUp.draw(win)
    lipDown.draw(win)

    # wait for click and then quit
    win.getMouse()
    win.close()


main()
