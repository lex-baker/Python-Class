#########################
# Author: Lex Baker
# Date: 9/6/22
# This is the answers and required coding for Lab 3
#########################

# Question 1
"""
name = input("Enter your name: ")
print("Hello,", name)
"""

# A:
# The argument passed to the input function was a String (str) type with a value of "Enter your name: "

# B:
# The return type was a String (str) with a value of "Lex"


# Question 2
"""
x = input("Enter a number: ")
type_of_x = type(x)
print("The variable x is of type: ", type_of_x)
y = input("Enter another number: ")
z = x + y
print("The sum of", x, "and", y, "is", z)
print("Twice", x, "is", 2*x)
"""

# A:
# A value of 56 was assigned to variable z. This is because the value assigned to x and y were strings, not integers, so adding them
# concatenated the strings rather than adding the numbers.

# B:
# Result: The variable x is of type:  <class 'str'>
# This backs up my assumption that z was the concatenation of two string variables.


# Question 3
"""
string_5 = "5"
string_6 = "6"
integer_5 = int(string_5)
integer_6 = int(string_6)
string_sum = string_5 + string_6
integer_sum = integer_5 + integer_6
print("Does",string_5,"plus",string_6,"equal",string_sum,"...")
print("or does",integer_5,"plus",integer_6,"equal",integer_sum)
"""

# A:
# The + operator in line 5 concatenates two strings together.

# B:
# The + operator in line 6 adds two integers togethers.

# C:
# No, the print statement doesn't only accept strings, as shown by the final line, when it prints three integers without error.


# Question 4
"""
side_length = eval(input("Enter a number: ")) # Eval fixes the int() vs float() issue, 
# by converting the argument to bytecode, evaluating as an expression, and returning the value
text1 = "A square of side length"
text2 = "has an area of"
print(text1, side_length, text2, side_length**2)
"""

"""
First, the input function is called and it displays its <argument(s)>, which has a value 
of <"Enter a number: ">, in the shell.  Once the user enters some text and hits the enter 
key, this text is sent back as the <return> value from the function.  The value that was 
returned replaces the input function call, and it becomes the <argument> for the call to 
the <int()> function.  The <int()> function takes this argument, which is of 
type <String/str>, converts it to type <Integer/int>, and returns the new value.  This 
returned value is then <passed> to the <function> named 
<print()>.
"""


# Question 5

# A:
# ValueError: invalid literal for int() with base 10: '2.5'
# This error occurs because the int() function can only convert string arguments the only contain whole numbers.
# 2.5 is a float, so int doesn't know what to do with the decimal.

# B:
# The float() function works the same as the int() function, only it converts strings to floats instead of whole integers.

# Question 6

# The fixed expression is "I ran " + str(26.2) + " miles."
# Error was thrown because integers cannot be concatenated with strings

# Question 8

tempF = float(input("What is the temperature in Fahrenheit: "))
tempC = (tempF - 32) * (5/9)
outputMessage = "Initial temp was " + str(tempF) + " degrees Fahrenheit, new temp is " + str(tempC) + " degrees Celsius"
print(outputMessage)
