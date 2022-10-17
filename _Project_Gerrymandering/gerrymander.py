from re import S
from graphics import *

state = input("Enter a state to find if it's gerrymandered: ").lower()

districts = open("districts.txt")
districts = districts.readlines()

for line in districts:
    s = line.split(",")[0].lower()
    if s == state:
        print(line)
print(state + " is not a state")