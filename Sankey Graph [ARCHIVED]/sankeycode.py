import sys
import math
import random
from graphics import *


def init(fileName):
    if(fileName == "--help"):
        help()
    try:
        file = open(os.path.join(sys.path[0], (fileName + ".txt")), "r")
        file.readline()
    except FileNotFoundError:
        print("No such file exists!")
        help()
    win = GraphWin(' ', 900, 900, autoflush=False)

    topText = Text(Point(win.getWidth() / 2, 100), file.readline()[:-1])
    topText.setStyle("bold")
    topText.setSize(20)
    topText.draw(win)

    leftText = Text(Point(65, win.getHeight() / 2 + 50), file.readline()[:-1])
    leftText.setSize(11)
    leftText.draw(win)

    fileText = Text(Point(25, win.getHeight() - 25), "FILE: " + fileName)
    fileText.setAlign("w")
    fileText.draw(win)

    creditText = Text(
        Point(win.getWidth() - 25, win.getHeight() - 25), "Created By: Lex Baker, 11/10/2021")
    creditText.setAlign("e")
    creditText.draw(win)

    scoreDict = makeDictionary(file)

    drawSankey(win, scoreDict)

    win.getMouse()
    win.close()


def makeDictionary(file):
    d = {}
    while(True):
        nL = file.readline()
        if(nL):
            d[nL[:nL.find(",")]] = float(nL[nL.find(",") + 1:-1])
        else:
            return d


def drawSankey(win, di):
    # In this function, the magic numbers 175, 200, 25, and 125 are used
    # 175 = The distance between the right side of the graph and the right side of the window
    # 200 = The distance between the left side of the plateau on the right of the graph and the right side of the window
    # 25 = The width of the plateaus on either side of the graph
    # 125 = The distance between the left side of the window and the left side of the graph
    total = 0.0
    for i in di:
        total += di[i]
    availPix = 600 - (len(di) - 1) * 10
    # Pixels per unit of flow
    ppf = availPix / total
    top = win.getHeight() / 2 - 250
    polyTop = (win.getHeight() / 2 + 50) - (total * ppf / 2)
    point1 = Point((win.getWidth() - 200), top)
    point2 = Point((win.getWidth() - 175), top)
    # Make these modifiable by user:
    # Color Base (The one on the left)
    cB = [60, 180, 75]
    # Color List, all colors that can be used (as of right now doesn't include the cB color)
    cL = [
        [230, 25, 75],
        [255, 225, 25],
        [0, 130, 200],
        [245, 130, 48],
        [70, 240, 240],
        [240, 50, 230],
        [0, 128, 128],
        [170, 110, 40],
        [255, 250, 200],
        [128, 0, 0],
        [170, 255, 195],
        [0, 0, 128],
        [128, 128, 128],
        [0, 0, 0]
    ]
    # Color Number, helps for iterating through cL. Might use different method or an interator
    cN = 0
    # not necessary if user chooses colors
    random.shuffle(cL)
    for i in di:
        point2.move(0, (di[i] * ppf))
        print((len(i) / 2) * 9.5)
        print(((win.getWidth() - 125) + int(len(i) * 10) / 2))

        # Working, kinda
        # newText = Text(Point(((win.getWidth() - 150) + (len(i) * 10) // 2), (point1.getY() + point2.getY()) / 2), i)

        # newText = Text(Point((8 *(win.getWidth() - 125) // 2), (point1.getY() + point2.getY()) / 2), i)
        # newText.setFace("courier")

        newText = Text(Point((win.getWidth() - 160), (point1.getY() + point2.getY()) / 2), i)
        newText.setSize(12)
        newText.setAlign("w")
        newText.draw(win)

        for x in range(((win.getWidth() - 175) - 125) + 1):
            zto = x / ((win.getWidth() - 175) - 125)
            x += 125
            slopedY = polyTop - (zto * (polyTop - point1.getY()))
            # This is unecessarily computationally intense
            # some solutions include making the first two if's only create one rectangle
            # instead of line make rectangles that are 2 or more pixels wide
            if(x <= 150):
                newLine = Line(Point(x, polyTop), Point(x, (polyTop + (di[i] * ppf))))
                win.plot(x, polyTop - 1, color="black")
                win.plot(x, (polyTop + (di[i] * ppf)), color="black")
            elif(x >= (win.getWidth() - 200)):
                newLine = Line(Point(x, point1.getY()), Point(x, point2.getY()))
                win.plot(x, point1.getY() - 1, color="black")
                win.plot(x, point2.getY(), color="black")
            else:
                zto = (math.sin(zto * math.pi - math.pi / 2) + 1) / 2
                slopedY = polyTop - (zto * (polyTop - point1.getY()))
                newLine = Line(Point(x, slopedY), Point(x, (slopedY + (di[i] * ppf))))
                win.plot(x, slopedY - 1, color="black")
                win.plot(x, (slopedY + (di[i] * ppf)), color="black")

            # Color will be each RBG value. first color will be multiplied by (1 - zto) and the second will be multiplied by zto. Then add
            a = int(cB[0] * (1 - zto) + (cL[cN][0] * (zto)))
            b = int(cB[1] * (1 - zto) + (cL[cN][1] * (zto)))
            c = int(cB[2] * (1 - zto) + (cL[cN][2] * (zto)))
            newLine.setFill(color_rgb(a, b, c))
            if(x == 125 or x == (win.getWidth() - 175)):
                newLine.setFill(color_rgb(0, 0, 0))
            newLine.draw(win)

        polyTop += di[i] * ppf
        point2.move(0, 10)
        point1 = Point((win.getWidth() - 200), point2.getY())
        if(cN > len(cL)):
            cN = 0
        else:
            cN += 1


def help():
    print("This program converts data files into an easily understood Sankey Graph.")
    print("More information on Sankey Graphs can be found here: https://www.data-to-viz.com/graph/sankey.html")
    # or something to cancel the program
    raise SystemExit(0)


init(input("What file do you want to graph: "))
