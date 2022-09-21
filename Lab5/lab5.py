"""
friday = True; 
print("friday is type: ", type(friday)); 
sunny = False; 
print("Is it sunny today?", sunny); 
#hawks_fan = true
"""
"""
##Exploring Boolean variables and logical operators 
tired = True; 
caffeinated = True; 
healthy = False; 
ready_to_learn = caffeinated or (not tired); 
excited_to_learn = caffeinated and (not tired); 
go_home = tired and (not healthy); 
print("Are you ready to learn? ", ready_to_learn); print("Are you EXCITED to learn!!? ", excited_to_learn); print("Should you go home? ", go_home); 

print('A'<'B')
print('a'<'A')
print('Z'<'a')
print('#'<'!')
print('cat'<'dog')
print('cap'<'cat')
"""
"""
##Uses an if-statement to control execution of two print commands 
number_donuts = int(input("How many donuts do you want? ")); 
less_than_half_dozen = number_donuts < 6; 
 	 
print("Mmmmm...eating", number_donuts, "donut(s) sounds yummy.") 
if less_than_half_dozen: 
    print("You know you are not getting the best value.")
    print("If you get a half-dozen or more, you get a discount.")
    print("You know what sounds even better?", number_donuts*2, "donuts."); 
"""

"""
##Uses if-else to run one group of statements or another
number = int(input("Enter an integer: "))
even_number = (number % 2) == 0
if even_number: 
    print(number, "is even.")
    print("Is",number,"also divisible by 4?",number%4==0)
else: 
    print(number, "is odd.")
    print("Is",number,"also divisible by 3?",number%3==0)
    print("What a great number.")

"""
"""
##Uses if-elif to sort through coffee possibilities
cream = False
sugar = True

if ((not cream) and (not sugar)): 
    preference = "black"
elif ((not cream) and sugar):     
        preference = "sweet"
elif (cream and (not sugar)):     
    preference = "white"
else: 
    preference = "regular"

print("You like your coffee " + preference) 
"""
"""
##Uses a while loop to make Python "count"
max_number = 15
counter = 0
while (counter < max_number): 
    print(counter);     
    #counter = counter+1; 
print("Good thing I incremented the counter or I would have counted FOREVER!!"); 
"""

"""
# code for problem 9
tired = input("Are you tired? (y/n)\n").lower()
if(tired == "y" or tired == "yes"):
    print("You should try to go to bed earlier.")
elif (tired != "n" and tired != "no"):
    print("You didn't enter y or n/yes or no...")
else:
    print("Congratulations on getting enough sleep!")
print("I hope you have a wonderful day!")
"""
"""
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")

if(num1 <= num2 and num1 <= num3):
    print(num1)
    if(num2 <= num3):
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
elif(num2 <= num1 and num2 <= num3):
    print(num2)
    if(num1 <= num3):
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
else:
    print(num3)
    if(num1 <= num2):
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)
"""

"""
num = int(input("Enter a positive integer:\n"))
sum = 0
fact = 1
while(num > 0):
    sum += num
    fact *= num
    num -= 1
print("sum =", sum)
print("factorial =", fact)
"""
import math

s1 = float(input("Enter the first side length:\n"))
s2 = float(input("Enter the second side length:\n"))
s3 = float(input("Enter the third side length:\n"))
if(s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1):
    print("The triangle you input is invalid")
else:
    a1 = math.acos((s2**2 + s3**2 - s1**2) / (2*s2*s3)) * (180/math.pi)
    a2 = math.acos((s1**2 + s3**2 - s2**2) / (2*s1*s3)) * (180/math.pi)
    a3 = math.acos((s1**2 + s2**2 - s3**2) / (2*s1*s2)) * (180/math.pi)
    print("The angles, in order, are:", end=" ")
    print(a1, a2, a3, sep=", ")