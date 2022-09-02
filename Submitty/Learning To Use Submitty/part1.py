#########################
# Author: Lex Baker
# Date: 8/31/22
# This program calculates Body Mass Index from height and weight inputted by user
#########################

# Get the user input
weight = eval(input("Enter your weight in pounds: "))
print(weight)
height_ft = eval(input("Enter your height in feet: "))
print(height_ft)
height_in = eval(input("Enter your remaining height in inches: "))
print(height_in)

# Converting and combining the two height inputs
height = (height_ft * 12) + height_in

# Calculating the BMI
BMI = (weight / height**2) * 703

# Round to two decimal places
BMI = round(BMI, 2)

#Return the value
print("Your BMI is", BMI)