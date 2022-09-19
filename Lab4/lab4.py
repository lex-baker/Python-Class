# TITLE:  Lab 04
# AUTHOR:  Lex Baker
# CLASS: Python
# CLASS MEETING TIME: Monday - Wednesday - Friday
# DATE: 9/13/22
# DATE SUBMITTED: 9/13/22
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

import sympy as sp;
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

for x in range(element)