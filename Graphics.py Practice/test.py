
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from graphics import *

def main():
    win = GraphWin("My Circle", 300, 300)
    leftEye = Circle(Point(80, 50), 5)
    leftEye.setFill('yellow')
    leftEye.setOutline('red')
    rightEye = leftEye.clone() # rightEye is exact copy of the left
    rightEye.move(20, 0)
    leftEye.draw(win)
    rightEye.draw(win)
    win.getMouse() #pause
    win.close() #close

main()