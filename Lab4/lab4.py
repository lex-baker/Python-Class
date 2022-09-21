# TITLE:  Lab 04
# AUTHOR:  Lex Baker
# CLASS: Python
# CLASS MEETING TIME: Monday - Wednesday - Friday
# DATE: 9/13/22
# DATE SUBMITTED: 9/20/22
# DESCRIPTION: Learning how to use Python for high level math

import math

print("The value of e is", math.e)
print(math.log(math.exp(2)))
print(math.sin(math.pi/2))
print(math.sin(math.pi))

import random

print(random.randint(5, 9))

# Chances of pulling the two of clubs when drawing 5 cards from a deck
# There is 1 card out of 52 total cards that we want
# There are 51 cards we don't care about
# We are drawing 5 cards, 1 of which needs to be the one we want
# For non-replacement probability, we use hypergeometric distribution
# Math is (1 choose 1) * (51 choose 4) / (52 choose 5)

num_1 = math.factorial(1) / (math.factorial(1) * math.factorial(1 -1))
num_2 = math.factorial(51) / (math.factorial(4) * math.factorial(51 - 4))
denom = math.factorial(52) / (math.factorial(5) * math.factorial(52 - 5))

print(num_1, num_2, denom)

prob = (num_1 * num_2) / denom
print("Probability of drawing the two of clubs when drawing 5 cards from a deck is ", round(prob * 100, 4), "%", sep="")

import sympy as sp
print(sp.sin(math.pi))
print(sp.sin(sp.pi))


print(sp.sqrt(8))
x,y = sp.symbols('x y')
expr = x + 2*y
print(expr)
expr + 1 - 2*y
print(expr)
print(sp.expand(x*(x+1)))
print(sp.factor(x**2 + 2*x*y + y**2))
print(sp.simplify(sp.sin(x)**2+sp.cos(x)**2))
expr=x*sp.sin(x*x)+1 
print(sp.diff(sp.cos(x), x))
f = sp.symbols('f', cls=sp.Function)
print(sp.dsolve(sp.Eq(f(x).diff(x, x) - 2*f(x).diff(x) + f(x), sp.sin(x)), f(x)))


import numpy as np
nparr = np.array([1, 2, 3, 4, 5])
print(np.sqrt(nparr))
print(np.square(nparr))
print(np.sin(nparr))



np.zeros((3,3))
m1 = np.array([[1,3],[5,7]])
m2 = np.identity(2)
print(m1, m2, sep="\n")
print(np.linalg.det(m1))
print(np.linalg.eig(m1))
print(np.linalg.inv(m1))
print(m1*m2)

m1.dot(m2)
a = np.matrix([[1,3],[5,7]])
b = np.matrix([[1,0],[0,1]])
print(a*b)

nums = np.array([2, 3, 5, 9, 9, 10, 11])
print("average =", np.average(nums))
print("variance =", np.var(nums))
print("std =", np.std(nums))

print(np.poly([2,3]))
print(np.roots([1,2,1]))

import matplotlib.pyplot as plt

"""
xVals = np.array([1,2,3,4])
yVals = xVals**2
plt.plot(xVals, yVals, "c*")
plt.show()

plt.plot(xVals, yVals, 'c*', label='Points')
plt.axis([0,5,0,18])
plt.title("Quadratic")
plt.grid(True)
plt.legend(loc='upper left')
plt.xlabel('x axis title')
plt.ylabel('y axis title')
plt.figtext(0.5, 0.5, "test")
plt.show()


x = np.arange(0, 5, 0.2)
plt.plot(x,x**2)
plt.plot(x,x)
plt.plot(x, np.cos(x))
plt.show()

"""

"""
t = np.arange(0., 5., 0.2)
plt.subplots_adjust(left=0.1,bottom=0.1,right=.9,top=.9,hspace=1)
plt.subplot(4,1,1) #num rows, num columns, fig number
plt.plot(t, 2**t, 'bs')
plt.title("exponential")
plt.subplot(4,1,2)
plt.plot(t, np.sin(t), 'r--')
plt.title("sine")
plt.subplot(4,1,3)
plt.plot(t, np.cos(t),'k')
plt.title("cosine")
plt.subplot(4,1,4)
plt.plot(t, np.log(t),'k')
plt.title("logarithmic")
plt.show()


mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000) 
plt.hist(x)
plt.title("Graphing Numpy Random Frequency")
plt.axis([0, 200, 0, 5000])
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

"""

scores = [71, 98, 80, 85, 85, 93, 74, 70, 88, 80, 91, 83, 82, 84, 84, 84, 84, 82, 80, 88, 79, 95, 87, 85, 90]
plt.hist(scores)
plt.title("Graphing Histogram")
plt.axis([60, 100, 0, 10])
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.grid(True)
plt.figtext(0.2, 0.8, "mean = " + str(np.average(scores)))
plt.figtext(0.2, 0.7, "std = " + str(np.std(scores)))
plt.show()