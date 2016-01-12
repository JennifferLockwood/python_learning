# exercise6-15.py

from graphics import *

def create_window():
    window = GraphWin("Sort of a Face", 400, 400)
    window.setBackground("white")
    window.setCoords(0.0, 0.0, 20.0, 20.0)
    return window

def drawFace(center, size, win):
    shape1 = Circle(center, size)
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

def main():    
    win = create_window()
    face = drawFace(Point(6.0, 6.0), 5, win)

    input("Press <Enter> to quit.")
    win.close()

main()
