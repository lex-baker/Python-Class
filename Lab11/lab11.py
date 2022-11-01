# Lex Baker
# Lab 11, Functions
# Submitted 11/1/22


x, y, z = 7, 23, 28

print("If the side is", x, "then the area is", x**2)

"""
Write a statement that calls the min function, passes it the arguments x, y, and z,
and assigns the return value to a variable named smallest.  Copy the statement below.
What was the end result of this statement?  
"""

smallest = min(x, y, z)
# print(smallest)

"""
Write an expression that calls the type function and passes it the expression x/2 as an
argument. What is the value returned by the type function, and what is done with this
value after the expression is evaluated?
"""

type(x/2)
# print(type(x/2))

"""
Write an expression that calls the chr function, passes it an argument of 72, and
passes the resulting return value directly into the type function.
"""

chr(72)
# # print(chr(72))
type(chr(72))
# print(type(chr(72)))