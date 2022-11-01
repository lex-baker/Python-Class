##turtlePolygon.py - Draws a polygon with a turtle
##Practice with functions, while loops and the turtle module

from turtle import *

def drawRegularPolygon(my_turtle, number_sides, side_length):
    """  Directs a turtle to draw a regular polygon """
    internal_angle = (number_sides - 2) * 180 / number_sides
    turn_angle = 180 - internal_angle

    side_number = 0
    while side_number < number_sides :
        my_turtle.fd(side_length)
        my_turtle.left(turn_angle)
        side_number += 1

##Main program
sides_input = int(input("Enter number of sides: "))
cage = Screen()
cage.setup(width=400, height=400, startx=0, starty=0)
bernie = Turtle(shape = "turtle")
# drawRegularPolygon(bernie,5,50)	
drawRegularPolygon(bernie,sides_input,50)