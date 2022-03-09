# Imports
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Convert list items to float
def floatList(myList):
    return [float(i) for i in myList]

# Flatten list
def flatten(myList):
    try:
        return [i for subList in myList for i in subList]
    except:
        return myList

# Initialize variables
x = sp.Symbol('x')
mir = 2 * x + 1
obj = x - 1
xBounds = (-5, 5)
xStep = 0.1
decPlaces = 4

# Approximate function zeros using Householder's method
def householderZeros(func, var, guess, order, epochs):
    for epoch in range(epochs):
        guessOld = guess
        guessOld += order * ((1 / func).diff(var, order - 1).subs(var, guessOld) / (1 / func).diff(var, order).subs(var, guessOld))
        guessOld = guessOld.evalf()
        if guessOld == sp.nan:
            break
        else:
            guess = guessOld
    return guess

# Normal line to function at a point
def norm(func, var, pt):
    return -1 / func.diff(var).subs(var, pt) * (var - pt) + func.subs(var, pt)

# Reflect point about center
def reflect(pt, center):
    return 2 * center - pt

ptsMir = np.arange(xBounds[0], xBounds[1] + xStep, xStep)
ptsObj = [sp.solve(norm(mir, x, ptMir) - obj) for ptMir in ptsMir]
ptsRefl = [reflect(ptObj[0], ptMir) for ptObj, ptMir in zip(ptsObj, ptsMir)]

ptsMir = floatList(flatten(ptsMir))
ptsObj = floatList(flatten(ptsObj))
ptsRefl = floatList(flatten(ptsRefl))

print('ptsObj:', ptsObj, '\n')
print('ptsMir:', ptsMir, '\n')
print('ptsRefl:', ptsRefl, '\n')

'''print(len(ptsObj), '\n')
print(len(ptsMir), '\n')
print(len(ptsRefl), '\n')'''