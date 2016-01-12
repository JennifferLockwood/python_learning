#Chapter 4 Exercise 4
#Write a program that draws a winter scene and some snowmen.

from graphics import *

def main():
    #head
    win = GraphWin('winter',800,450)

    #background
    win.setBackground('darkgrey')

    #snow
    sn = Rectangle(Point(0,170), Point(800,450))
    sn.setFill('white')
    sn.draw(win)

    #trees
    tr = Polygon(Point(60,300), Point(120,50), Point(180,300))
    tr.setFill('green')
    tr.draw(win)

    tr = Polygon(Point(200,200), Point(230,70), Point(260,200))
    tr.setFill('green')
    tr.draw(win)

    tr = Polygon(Point(500,300), Point(550,40), Point(600,300))
    tr.setFill('green')
    tr.draw(win)

    tr = Polygon(Point(600,350), Point(670,50), Point(740,350))
    tr.setFill('green')
    tr.draw(win)

    #snowman
    s = Circle(Point(400,300),80)
    s.setFill('white')
    s.draw(win)

    s = Circle(Point(400,210),50)
    s.setFill('white')
    s.draw(win)

    s = Circle(Point(400,145),30)
    s.setFill('white')
    s.draw(win)

    #coal
    c = Circle(Point(390,140),5)
    c.setFill('black')
    c.draw(win)

    c = Circle(Point(410,140),5)
    c.setFill('black')
    c.draw(win)

    c = Circle(Point(386,158),4)
    c.setFill('black')
    c.draw(win)

    c = Circle(Point(400,163),4)
    c.setFill('black')
    c.draw(win)

    c = Circle(Point(414,158),4)
    c.setFill('black')
    c.draw(win)


    win.getMouse() # pause for click in window
    win.close()

main()
