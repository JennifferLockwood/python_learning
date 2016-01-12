# exercise4-1-c.py
# Exercise 1, item c, Chapter 4

from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(50,50), Point(75,75))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shapeSe = shape.clone()        
        shapeSe.move(dx, dy)
        shapeSe.draw(win)
        
    message = Text(Point(80, 10),"Click again to quit")
    message.draw(win)
    win.getMouse()
    win.close()

    
main()

