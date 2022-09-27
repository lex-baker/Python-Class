# Author: Lex Baker
# Date: 9/27/22
# This is my code for Lab 6


"""
#Example of a bad way to get input
my_number = int(input("I demand an integer."))
print("I got",my_number)
"""
"""
#Example of a better way to get input
try:
    my_number = int(input("I demand an integer: "))
    print("I got",my_number)
except ValueError:
    print("I don't have an integer, but I am not broken!")
"""
"""
#Example of a robust way to get input
my_number = None
while my_number == None:
    try:
        my_number = int(input("I demand an integer: "))
    except ValueError:
        print("I am not broken, and I am not going away")

print("I got ",my_number,". I knew I would win!!",sep = "")
"""

# Lab 5 rework
import math
a1 = None
a2 = None
a3 = None
while a1 == None or a2 == None or a3 == None:
    s1 = float(input("Enter the first side length:\n"))
    s2 = float(input("Enter the second side length:\n"))
    s3 = float(input("Enter the third side length:\n"))
    
    try:
        a1 = math.acos((s2**2 + s3**2 - s1**2) / (2*s2*s3)) * (180/math.pi)
        a2 = math.acos((s1**2 + s3**2 - s2**2) / (2*s1*s3)) * (180/math.pi)
        a3 = math.acos((s1**2 + s2**2 - s3**2) / (2*s1*s2)) * (180/math.pi)
        print("The angles, in order, are:", end=" ")
        print(a1, a2, a3, sep=", ")
    except ValueError:
        print("The triangle lengths you input are invalid")