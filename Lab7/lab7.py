# TITLE:  Lab 07
# AUTHOR:  Lex Baker
# CLASS: Python
# CLASS MEETING TIME: Monday - Wednesday - Friday
# DATE: 10/4/22
# DATE SUBMITTED: 10/4/22

from turtle import *
from shapely.geometry import Polygon, Point, LineString, MultiPolygon
from shapely_graphics import *
import matplotlib.pyplot as plt
import math


def first():
    canvas = Screen(); # create screen object named canvas
    canvas.setup(500,500); # set screen size to 500x500 pixels
    t = Turtle(); 
    t.color("black");
    t.penup()
    t.right(90)
    t.forward(100)
    t.pendown()
    t.circle(100);
    t.penup();
    t.goto(0,-50);
    t.pendown();
    t.color("red")
    t.write("Circle");
    canvas.exitonclick(); 

#first()

def polygon():
    length = int(input("Length of the sides: "))
    sides = int(input("Number of sides: "))
    degPerAngle = 180 - (((sides - 2) * 180) / sides)
    print(degPerAngle)

    canvas = Screen()
    canvas.setup(500,500)
    t = Turtle()
    i = 0
    while i < sides:
        t.forward(length)
        t.left(degPerAngle)
        i += 1
    canvas.exitonclick()

#polygon()

def shapely():
    p1 = Point(0,1);
    p2  = Point(1,2);
    print(p1.distance(p2));
    x1 = LineString([(0,0), (1,1)]);
    x2 = LineString([(1,0),(0,1)]);
    print(x1.intersection(x2));
    print()
    triangle = Polygon([(0,0),(1,0),(0,1)]); 
    print(triangle.area);
    print(triangle.length);
    c = triangle.centroid;
    print(type(c))
    print(c.coords[:]);
    print(c.x);
    print(c.y);

#shapely()

def more_shapely():
    triangle = Polygon([(0,0),(1,0),(0,1)]); # creating triangle object assigned to variable triangle
    triangle_a = scale(triangle, xfact=2, yfact=2); # creates triangle_a, which is scaled by a factor of 2 from triangle
    print(triangle_a.exterior.coords[:]);
    triangle_b = translate(triangle,3,4);
    print(triangle_b.exterior.coords[:]);
    triangle_c = rotate(triangle,45,(0,0), False);
    print(triangle_c.exterior.coords[:]);
    # Imported from the shapely_graphics module
    plt.grid(True)
    plot_polygon(triangle)
    plot_polygon(triangle_a, "b")
    plot_polygon(triangle_b, "g")
    plot_polygon(triangle_c, "y")
    plt.figtext(0.2, 0.7, "triangle is red (or purple)\ntriangle_a is blue\ntriangle_b is green\ntriangle_c is yellow")
    plt.show()
#more_shapely()

def triangulation():
    side1 = int(input("Enter the first side length in pixels (10-400): "))
    if side1 < 10 or side1 > 400: print("Invalid length"); triangulation(); 
    side2 = int(input("Enter second side length in pixels (10-400): "))
    if side2 < 10 or side2 > 400: print("Invalid length"); triangulation(); 
    angle3 = float(input("Enter angle between the two in degrees (1-179): "))
    if angle3 < 1 or angle3 > 179: print("Invalid angle"); triangulation(); 

    side3 = math.sqrt(side1**2 + side2**2 - 2 * side1 * side2 * math.cos(angle3 * (math.pi / 180)))
    print("Third side's length =", round(side3, 2))
    angle1 = math.asin((math.sin(angle3 * (math.pi / 180)) / side3) * side1) * (180 / math.pi)
    angle2 = 180 - angle1 - angle3
    print("The other two angles are", round(angle1, 2), "and", round(angle2, 2))
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    print("The area of the triangle is", round(area, 2))

    height = (2 * area) / side1
    print("height is", height)
    # So the third point of a scalene triangle, when point 1 is at (0, 0) and point two is at (base of triangle, 0)
    # is (x3, height of triangle)
    # x3 = x1 +/- sqrt( -(height ^ 2) + (2 * height * y1) + (distance or third side length)^2 - (y1 ^ 2) )
    # Additionally, we know that x1 = 0 and y1 = 0, so
    # x3 = +/- sqrt( (distance ^ 2) - (height ^ 2) )
    x3 = math.sqrt(side3**2 - height**2)
    verts = [[0, 0], [side1, 0], [x3, height]]

    t = Turtle()
    canvas = Screen()
    canvas.setup(500, 500)
    t.hideturtle()
    t.color("blue")
    t.penup()
    centroidX = (verts[0][0] + verts[1][0] + verts[2][0]) / 3
    centroidY = (verts[0][1] + verts[1][1] + verts[2][1]) / 3
    print(centroidX, centroidY)
    for i, coord in enumerate(verts):
        verts[i] = [coord[0] - centroidX, coord[1] - centroidY]
    t.goto(verts[0][0], verts[0][1])
    t.setheading(0)
    t.showturtle()
    t.pendown()
    t.write(t.pos())
    t.forward(side1)
    t.left(180 - angle3)
    t.write(t.pos())
    t.forward(side2)
    t.left(180 - angle1)
    t.write(t.pos())
    t.forward(side3)
    t.penup()
    t.goto(0, verts[0][1] - 20)
    t.pendown()
    t.write("Here is your triangle!")
    t.hideturtle()
    canvas.exitonclick(); 

#triangulation()


def tri_with_shapely():
    side1 = int(input("Enter the first side length in pixels (10-400): "))
    if side1 < 10 or side1 > 400: print("Invalid length"); triangulation(); 
    side2 = int(input("Enter second side length in pixels (10-400): "))
    if side2 < 10 or side2 > 400: print("Invalid length"); triangulation(); 
    angle3 = float(input("Enter angle between the two in degrees (1-179): "))
    if angle3 < 1 or angle3 > 179: print("Invalid angle"); triangulation(); 

    side3 = math.sqrt(side1**2 + side2**2 - 2 * side1 * side2 * math.cos(angle3 * (math.pi / 180)))
    print("Third side's length =", round(side3, 2))
    angle1 = math.asin((math.sin(angle3 * (math.pi / 180)) / side3) * side1) * (180 / math.pi)
    angle2 = 180 - angle1 - angle3
    print("The other two angles are", round(angle1, 2), "and", round(angle2, 2))
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    print("The area of the triangle is", round(area, 2))

    height = (2 * area) / side1
    print("height is", height)
    # So the third point of a scalene triangle, when point 1 is at (0, 0) and point two is at (base of triangle, 0)
    # is (x3, height of triangle)
    # x3 = x1 +/- sqrt( -(height ^ 2) + (2 * height * y1) + (distance or third side length)^2 - (y1 ^ 2) )
    # Additionally, we know that x1 = 0 and y1 = 0, so
    # x3 = +/- sqrt( (distance ^ 2) - (height ^ 2) )
    x3 = math.sqrt(side3**2 - height**2)
    verts = [(0, 0), (side1, 0), (x3, height)]
    triangle = Polygon(verts)
    c = triangle.centroid
    for i, coord in enumerate(verts):
        verts[i] = [round(coord[0] - c.x, 2), round(coord[1] - c.y, 2)]
    triangle = translate(triangle, -c.x, -c.y)
    plt.grid(True)
    plot_polygon(triangle)
    plt.text(verts[0][0],  verts[0][1], verts[0])
    plt.text(verts[1][0],  verts[1][1], verts[1])
    plt.text(verts[2][0],  verts[2][1], verts[2])
    plt.text(0, -3 - c.y, "This is a triangle!")
    plt.show()

#tri_with_shapely()


def tessellation_turtle():
    sides = int(input("Enter the number of sides: "))
    length = 50
    angle = 180 * (sides-2) / sides
    if(360 % angle != 0):
        print("This shape cannot be tessellated because 360 is not a multiple of one of its interior angles")
        return
    screen = Screen()
    t = Turtle()
    t.right(45)
    t.dot()
    for i in range(int(360 / angle)):
        t.circle(length, 360, sides)
        t.left(angle)
    screen.exitonclick()

#tessellation_turtle()

def tessellation_shapely():
    sides = int(input("Enter the number of sides: "))
    angle = 180 * (sides-2) / sides
    rads = angle * (math.pi / 180)
    length = 50
    if(360 % angle != 0):
        print("This shape cannot be tessellated because 360 is not a multiple of one of its interior angles")
        return
    plt.grid(True)
    for i in range(int(360 / angle)):
        # draw line
        # rotate by angle
        # repeat until final vertex equals original vertex
        firstV = (0,0)
        nextV = (0,0)
        for x in range(sides):
            print("firstV: ", firstV)
            print("nextV = ", nextV)
            firstV = nextV
            nextV = (firstV[0] + length * math.cos(rads), firstV[1] + length * math.sin(rads))
            line = LineString([firstV, nextV])
            plot_line(line)
            rads += math.pi / (sides / 2)
        rads += math.pi / (int(360 / angle) / 2)
    plt.show()

tessellation_shapely()

