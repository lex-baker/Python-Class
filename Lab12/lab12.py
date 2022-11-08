# Author: Lex Baker
# Created: 11/8/22
# Lab 12, Exploring Scope

def shadowing(same):
    same2 = "world"
    print("First from function: ", same, same2) # Returns: First from function:  21 world
    same += 5
    same2 = "helloW"
    print("Second from function: ", same, same2) # Returns: Second from function:  26 helloW
    
same = 10
same2 = "hello"
print("First from main: ", same, same2) # Returns: First from main:  10 hello
shadowing(21)
print("Second from main: ", same, same2) # Returns: Second from main:  10 hello