import sys
from graphics import *
import math
import random

def init(fileName):
  try:
    #file = open((fileName + ".txt"), "r")
    file = open(os.path.join(sys.path[0], (fileName + ".txt")), "r")
    print(file.readline())
  except:
    print("No such file exists!")
    #or something to cancel the program
    raise SystemExit(0)

  win = GraphWin(' ', 900, 900)

  topText = Text(Point(win.getWidth()/2, 100), file.readline()[:-1])
  topText.setStyle("bold")
  topText.setSize(20)
  topText.draw(win)

  leftText = Text(Point(75, win.getHeight()/2), file.readline()[:-1])
  leftText.draw(win)

  fileText = Text(Point(100, win.getHeight() - 25), "FILE: " + fileName)
  fileText.draw(win)

  creditText = Text(Point(win.getWidth() - 150, win.getHeight() - 25), "Created By: Lex Baker, 11/10/2021")
  creditText.draw(win)

  scoreDict = makeDictionary(file)
  #print(scoreDict)

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
  total = 0.0
  #short = len(list(di.keys())[0])
  for i in di:
    total += di[i]
    #if(len(i) < short): short = len(i)
  availPix = 600 - (len(di) - 1) * 10
  ppf = availPix / total
  #The left and right were for the right-side boxes
  left = win.getWidth() - 200
  right = win.getWidth() - 175
  top = win.getHeight() / 2 - 250
  polyTop = (win.getHeight()/2 + 50) - (total * ppf / 2)
  point1 = Point(left, top)
  point2 = Point(right, top)
  #Make this modifiable by user
  userBaseColor = [60, 180, 75]
  cL = [[230, 25, 75], [255, 225, 25], [0, 130, 200], [245, 130, 48], [70, 240, 240], [240, 50, 230], [0, 128, 128], [170, 110, 40], [255, 250, 200], [128, 0, 0], [170, 255, 195], [0, 0, 128], [128, 128, 128], [0, 0, 0]]
  #not necessary if user chooses colors
  random.shuffle(cL)
  cN = 0
  for i in di:
    point2.move(0, (di[i] * ppf))
    newText = Text(Point((win.getWidth() - 88), (point1.getY() + point2.getY()) / 2), i)
    newText.draw(win)

    #slope = (polyTop - point1.getY()) / (200 - point1.getX())
    #the formula for this is y = slope * x + 200
    #print(slope)

    for x in range(((win.getWidth() - 175) - 125) + 1):
      zto = x / ((win.getWidth() - 175) - 125)
      x += 125
      slopedY = polyTop - (zto * (polyTop - point1.getY()))
      #while x < 200 or x > (-200) dont use a slope, just make rectangles
      if(x <= 150):
        newLine = Line(Point(x, polyTop), Point(x, (polyTop + (di[i] * ppf))))
        win.plot(x, polyTop - 1, color="black")
        win.plot(x, (polyTop + (di[i] * ppf)), color="black")
      elif(x >= (win.getWidth() - 200)):
        newLine = Line(Point(x, point1.getY()), Point(x, point2.getY()))
        win.plot(x, point1.getY() - 1, color="black")
        win.plot(x, point2.getY(), color="black")
      else:
        #slopedY = (x - 200) * slope + polyTop

        zto = (math.sin(zto * math.pi - math.pi / 2 ) + 1) / 2
        slopedY = polyTop - (zto * (polyTop - point1.getY()))
        newLine = Line(Point(x, slopedY), Point(x, (slopedY + (di[i] * ppf))))
        win.plot(x, slopedY - 1, color="black")
        win.plot(x, (slopedY + (di[i] * ppf)), color="black")
      
      
      #Color will be each RBG value. first color will be multiplied by (1 - zto) and the second will be multiplied by zto. Then add
      a = int(userBaseColor[0] * (1 - zto) + (cL[cN][0] * (zto)))
      b = int(userBaseColor[1] * (1 - zto) + (cL[cN][1] * (zto)))
      c = int(userBaseColor[2] * (1 - zto) + (cL[cN][2] * (zto)))
      newLine.setFill(color_rgb(a, b, c))
      if(x == 125 or x == (win.getWidth() - 175)): newLine.setFill(color_rgb(0, 0, 0))
      newLine.draw(win)

    """
    
    newRect = Rectangle(point1, point2)
    newRect.setFill(cL[cN])
    newRect.draw(win)

    newPoly = Polygon(Point(200, polyTop), point1, Point(left, point2.getY()), Point(200, (polyTop + (di[i] * ppf))))
    #newPoly = Polygon(Point(200, 150), Point(500, 150), Point(500, 130), Point(200, 130))
    newPoly.setFill(cL[cN])
    newPoly.draw(win)
    
    """

    polyTop += di[i] * ppf
    point2.move(0, 10)
    point1 = Point(left, point2.getY())
    if(cN > len(cL)): cN = 0
    else: cN += 1

  """
  sourceRect = Rectangle(Point(175, (win.getHeight()/2 + 50) - (total * ppf / 2)), Point(200, (win.getHeight()/2 + 50) + (total * ppf / 2)))
  sourceRect.setOutline("black")
  sourceRect.setFill("#3cb44b")
  sourceRect.draw(win)
  """


init(input("What file do you want to graph: "))