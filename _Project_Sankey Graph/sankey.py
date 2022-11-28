import sys
from graphics import *
import math
import random

def main():
  # Get user input for file name
  fileName = input("What file do you want to graph: ")
  # Try-Except block to safely open the file
  # Returns an error if not found instead of crashing
  try:
    file = open((fileName + ".txt"), "r")
    #file = open(os.path.join(sys.path[0], (fileName + ".txt")), "r")
  except:
    # If file is not found, alert the user and end the program
    print("No such file exists!")
    exit()

  # Iterate through first three known values of each file, the comment, the title, and the left side label

  # First line just needs to be iterated through
  file.readline()
  # .strip() to remove any newline characters or unneccessary whitespace
  title = file.readline().strip()
  left_label = file.readline().strip()


  # Create the GraphWin object, at 900 by 900 pixels
  win = GraphWin(' ', 900, 900)

  # Create the title text, set formatting, draw to GraphWin
  topText = Text(Point(win.getWidth()/2, 100), title)
  topText.setStyle("bold")
  topText.setSize(20)
  topText.draw(win)

  # Create the left label text, draw to GraphWin
  leftText = Text(Point(75, win.getHeight()/2), left_label)
  leftText.draw(win)

  # Create file name informational text, draw to GraphWin
  fileText = Text(Point(100, win.getHeight() - 25), "FILE: " + fileName)
  fileText.draw(win)

  # Create author and date text, draw to GraphWin
  creditText = Text(Point(win.getWidth() - 150, win.getHeight() - 25), "Created By: Lex Baker, 11/10/2021")
  creditText.draw(win)

  # Create the dictionary of labels and their data points
  dataDict = makeDictionary(file)
  #print(scoreDict)

  # Draw the full sankey graph to the GraphWin object, using the dictionary of scores
  drawSankey(win, dataDict)

  # Wait until user clicks on the canvas to close the window
  win.getMouse()
  win.close()

  

def makeDictionary(file):
  # Initialize the dictionary
  d = {}
  # Read the next line (technically the fourth in the file, since three were already read)
  line = file.readline()
  # Loop until file runs out of lines
  while line:
    # This if statement checks to make sure the line being added to the dictionary
    # isn't commented out and contains a comma, easily checking for malformed data
    if line[0] != "#" and line.find(",") != -1:
      # Split the line into two values on either side of the comma
      split = line.split(",")
      # Add to dictionary with key being the label and value being the data point
      d[split[0]] = float(split[1])
    # Read the next line
    line = file.readline()

  return d

def drawSankey(win, info):
  total = 0.0
  for i in info:
    total += info[i]
  availPix = 600 - (len(info) - 1) * 10
  ppf = availPix / total
  #The left and right were for the right-side boxes
  left = win.getWidth() - 200
  right = win.getWidth() - 175
  top = win.getHeight() / 2 - 250
  polyTop = (win.getHeight()/2 + 50) - (total * ppf / 2)
  point1 = Point(left, top)
  point2 = Point(right, top)
  #Make this modifiable by user
  # Base color, aka the color on the left side of the graph
  userBaseColor = [60, 180, 75]
  # Color list, all possible colors that can be used on the left side (assigned randomly)
  color_list = [[230, 25, 75], [255, 225, 25], [0, 130, 200], [245, 130, 48], [70, 240, 240], [240, 50, 230], [0, 128, 128], [170, 110, 40], [255, 250, 200], [128, 0, 0], [170, 255, 195], [0, 0, 128], [128, 128, 128], [0, 0, 0]]
  # Not necessary if user chooses colors
  random.shuffle(color_list)
  color_number = 0
  for i in info:
    point2.move(0, (info[i] * ppf))
    newText = Text(Point((win.getWidth() - 88), (point1.getY() + point2.getY()) / 2), i)
    newText.draw(win)

    for x in range(125, (win.getWidth() - 175) + 1):
      # zto is a float that represents how far along the lines have gotten, with the first line being 0 and the last being 1
      zto = (x - 125) / ((win.getWidth() - 175) - 125)

      zto = (math.sin(zto * math.pi - math.pi / 2 ) + 1) / 2
      # print(zto)

      slopedY = polyTop - (zto * (polyTop - point1.getY()))
      newLine = Line(Point(x, slopedY), Point(x, (slopedY + (info[i] * ppf))))

      # These two lines place a single black pixel at both ends of each line to give a smooth black border to the entire graph
      win.plot(x, slopedY - 1, color="black")
      win.plot(x, (slopedY + (info[i] * ppf)), color="black")
        
      

      # This section is for creating the smooth color gradient
      
      if(zto == 0 or zto == 1):
        # If the line is the first or the last one, make it black to outline the graph
        newLine.setFill(color_rgb(0, 0, 0))
      else:
        # Color will be each RBG value. First color will be multiplied by (1 - zto) and the second will be multiplied by zto. Then add both
        r = int(userBaseColor[0] * (1 - zto) + (color_list[color_number][0] * (zto)))
        g = int(userBaseColor[1] * (1 - zto) + (color_list[color_number][1] * (zto)))
        b = int(userBaseColor[2] * (1 - zto) + (color_list[color_number][2] * (zto)))
        newLine.setFill(color_rgb(r, g, b))

      newLine.draw(win)

    polyTop += info[i] * ppf
    point2.move(0, 10)
    point1 = Point(left, point2.getY())
    if(color_number > len(color_list)):
      color_number = 0
    else: 
      color_number += 1

if __name__ == "__main__":
  main()
  #print(makeDictionary(open("Baseball.txt")))