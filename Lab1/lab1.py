# TITLE:  Lab 01: print()
# AUTHOR:  Lex Baker
# CLASS: Python
# CLASS MEETING TIME: Monday - Wednesday - Friday
# DATE: 8/23/22
# DATE SUBMITTED: date you submitted your solution (ideally by the Friday of the same week)
# DESCRIPTION: Learning how to use Python to print to the console/terminal

# Question 1
print("Hello World"); 
print("Hello World"); 
print("Hello","World"); 
# A. No difference
print("Hello","World,","This","Is","My","First","Program"); 
# B. Yes

# C. Not sure if this is a question, but I've seen arguments against the usage of semicolons in Python as fluff.
# Additionally, most IDEs mark them as errors, such as Visual Studio Code, which marks them in red on usage.
# The popular Python formatting guide, Pep8, only references them in relation to multi-line statements, and even then discourages their use
# The core argument is that semicolons aren't "Pythonic", and go against the goal/style of the language.

# Question 2
print("Hello", "World"); 
print   ("Hello ", "World"); 
# A. When the extra space is within the quotation marks
# B. Between the parentheses, quotion marks, and commas. You can also add space between the print statement and the opening parenthesis

# Question 3
#Print("Hello")
# This throws the error: name "Print" is not defined
print("Hello"); 

# Question 4
print(); 
print(); 
# A. Without string argument, print() simply prints to a newline.
print("I","love","coding!", sep = "+"); 
print("Two","four","six","eight",sep = ", ", end = "; "); 
print("who do we appreciate?"); 
# B. The "sep" parameter allows for a modification of the seperator characters added when a comma is used outside of quotations
# The "end" parameter allows for modification to the characters printed after the characters in quotes are printed.

# Question 5
# A. The use of the \ character
print("She said \"Hello.\""); 
# B.
print("She said \"Hello, have you said the word \'python\' yet today?\""); 
# C. \t inserts a tab character, and \n goes to a new line (equivalent to pressing enter)
# D. Triple quotes allow for multi-line strings. These are popular for long strings and comments in python files,
# because python doesn't parse strings that just exist in the file

# Quick Check A
print("spam", "eggs", sep="+")

# Quick Check B
print("Yay!\nIt's summer!")