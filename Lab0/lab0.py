#########################
# Name: Lex Baker
# Course: CSC110, Semester 1, Python for Scientists
# Date: 8/16/2022
# Filename: lab0.py
# Peers: N/A
# References:
#########################

#### Introduction
from re import X


print("Step 0: Answer\n")
#### Step #0 - On which device did you install Thonny?
# I use my own IDE

# Question 3: This program is printing the values of variables, 
# and then printing the result of subtracting the two

age = 20
year = 2020
print(age)
print(year)
print(year-age)
year_born = year - age
print("You are", age, "years old")
print("You were born in", year_born)



print("Step 1: Answer\n")
#### Step #1

#Variation 1
name = "Alex"
school = "SC GSSM"
age = 16
print(name,"goes to", school, "and is", age, "years old")

#Variation 2
name = "Jordan" #"Noa"
scgiik = "Smith College" #"Coker College"
age = 33 #20
year = 2020
print(name, "goes to", scgiik, "and is", age, "years old")
print(name, "was born in", year - age)



print("Step 2: Answer\n")
#### Step #2

#Multiply a printed variable by a set amount
word1 = "hello"
word2 = "there!"
#print(word1 * 2)
#print(word1 * 5)
#print(word2 * 10)
print((word1 + " ") * 4 + word2)
print(word1, (word2 + " ") * 5 + word1)



print("Step 3: Answer\n")
#### Step #3

print((word1 + word2) * 5)

print("Step 4: Answer\n")
#### Step #4

#Iterate over a loop, and print the name and dashes equal to the amount of characters in the name
for name in ["Aleah", "Belle", "Chen", "Jack", "Tom", "Bob"]:
    print(name, "-" * len(name))


print("Step 5: Answer\n")
#### Step #5

#Iterate over a loop, and print dashes equal to the amount of characters in the name
for name in ["Aleah", "Belle", "Chen", "Jack", "Tom", "Bob"]:
    print(name)
    print("-" * len(name))



print("Step 6: Answer\n")
#### Step #6

#Put the same amount of dashes as characters in the name above and below the name
for name in ["Aleah", "Belle", "Chen", "Jack", "Tom", "Bob"]:
    print("-" * len(name))
    print(name)
    print("-" * len(name))
    print()



print("Step 7: Answer\n")
#### Step #7

#Iterate through a loop to see how the length of names affects the variables.
for name in ["Julia Child", "Gloria Steinem"]:
    nameLen = len(name)
    nameLen4 = len(name) + 4
    nameLen2 = len(name) + 2
    x = 10
    bar1 = "-" * x 
    bar2 = bar1 + "|"
    bar3 = "<" + bar1 + ">"
    bar4 = "-" * nameLen

    print("name =", name)
    print("nameLen =", nameLen)
    print("nameLen4 =", nameLen4)
    print("nameLen2 =", nameLen2)
    print("x =", x)
    print("bar1 =", bar1)
    print("bar2 =", bar2)
    print("bar3 =", bar3)
    print("bar4 =", bar4)

print()
#Step 7C

#Print a box around each name
for name in ["Aleah", "Belle", "Chen", "Jack", "Tom", "Bob"]:
    print("", "-" * len(name))
    print("|" + name + "|")
    print("", "-" * len(name))
    print()


print("Step 8: Answer\n")
#### Step #8
# My primary concern lies in the black box nature of most widely used AI models
# While security is a concern for all, not being able to check for bias
# can lead to even more problems down the road.
# To solve this, companies should allow select security researchers who
# aren't affiliated with the company to vet the work done.


print("Bonus\n")
#### Bonus


