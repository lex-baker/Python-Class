import sys
from graphics import *
import math
import random

def main():
  # Get user input for file name
  fileName = input("What file do you want to graph: ")
  # If user enters --help
  if(fileName == "--help"):
        help()
  # Try-Except block to safely open the file
  # Returns an error and help message if not found instead of crashing
  try:
    file = open((fileName + ".txt"), "r")
    #file = open(os.path.join(sys.path[0], (fileName + ".txt")), "r")
  except FileNotFoundError:
    # If file is not found, alert the user and end the program
    print("No such file exists!")
    help()

  # Iterate through first three known values of each file, the comment, the title, and the left side label

  # First line just needs to be iterated through
  file.readline()
  # .strip() to remove any newline characters or unneccessary whitespace
  title = file.readline().strip()
  left_label = file.readline().strip()


  # Create the GraphWin object, at 900 by 900 pixels
  win = GraphWin(' ', 900, 900, autoflush=False)

  # Set background to grey
  win.setBackground("grey")

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

  # Save the graph as [filename].ps
  # win.postscript(file = fileName + ".ps", colormode = "color") 

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
  """Function that takes the data and the canvas and creates the actual sankey diagram"""
  # Defining constants
  
  # total stores the total of all values from the data
  total = 0.0
  for i in info:
    total += info[i]
  
  available_pixels = 600 - (len(info) - 1) * 10
  
  # Calculate the number of pixels per flow by dividing the amount of pixels avaiable by the total number of all data
  # Allows for the conversion from values to relative size in pixels
  pixels_per_flow = available_pixels / total # pixels per something, frame? line? 
  #The left and right were for the right-side boxes
  left = win.getWidth() - 200
  right = win.getWidth() - 175
  top = win.getHeight() / 2 - 250
  polyTop = (win.getHeight()/2 + 50) - (total * pixels_per_flow / 2)
  point1 = Point(left, top)
  point2 = Point(right, top)

  # Base color, aka the color on the left side of the graph
  userBaseColor = [60, 180, 75]
  # Color list, all possible colors that can be used on the left side (assigned randomly)
  color_list = [
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
    [0, 0, 0]
  ]
  
  # Randomly choose colors from the predefined color list
  color_number = random.randrange(len(color_list))

  # For each data point in the dictionary
  for i in info:
    # Store the value of the length of the lines for each data point
    line_length = info[i] * pixels_per_flow
    # For each line, move point2 down to the bottom of the line
    point2.move(0, line_length)
    newText = Text(Point((win.getWidth() - 88), (point1.getY() + point2.getY()) / 2), i)
    newText.draw(win)

    for x in range(125, (win.getWidth() - 175) + 1):
      # zto, or zero-to-one, is a float that represents how far along the lines have gotten, with the first line being 0 and the last being 1
      # When first intialized, zto is a linear trend
      zto = (x - 125) / ((win.getWidth() - 175) - 125)

      # Smoothing out zto by making it a sin curve instead of a linear trend
      zto = (math.sin( zto * math.pi - math.pi / 2 ) + 1) / 2

      # The top of the line being drawn, sized using zto
      slopedY = polyTop - (zto * (polyTop - point1.getY()))

      # Creating the line object
      newLine = Line(Point(x, slopedY), Point(x, (slopedY + line_length)))

      # This places a single black pixel at both ends of each line to give a smooth black border to the entire graph
      win.plot(x, slopedY - 1, color="black")
      win.plot(x, (slopedY + line_length), color="black")
              

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

    polyTop += line_length
    point2.move(0, 10)
    point1 = Point(left, point2.getY())
    
    # Choose another random color
    color_number = random.randrange(len(color_list))
  
def help():
  """This function returns a help message if the user mistypes the filename or inputs --help"""
  print("This program converts data files into an easily understood Sankey Graph.")
  print("More information on Sankey Graphs can be found here: https://www.data-to-viz.com/graph/sankey.html")
  # Exit the program
  exit()
  
if __name__ == "__main__":
  main()
  #print(makeDictionary(open("Baseball.txt")))