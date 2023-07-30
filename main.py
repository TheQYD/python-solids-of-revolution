#!/usr/bin/env python3 

'''
Volume of Solids of Revolution Calculator
'''

from sympy import Integral, Symbol, sympify

import math
import sys


# Global Variables
axes = ('x', 'y')
bump = "\n" + "_" * 80 + "\n"

# If the axis of rotation is parallel to the functions:
def discMethod(functions, x, interval):
  a = interval[0]
  b = interval[1]
  f = functions[0]
  g = functions[1]
  
  v = abs(f ** 2 - g ** 2)              # absolute value of f squared - g squared
  v = Integral(v, (x, a, b)).doit()     # integrate f ** 2 - g ** 2
  #v = math.pi * v                       # multiply by pi
  v = "pi " + str(v)
  return v


# If the axis of rotation is perpendicular to the functions:
def shellMethod(functions, x, interval):
  a = interval[0]
  b = interval[1]
  f = functions[0]
  g = functions[1]

  v = x * abs(f - g)                    # absolute value of f - g
  v = Integral(v, (x, a, b)).doit()     # integrate x * (f - g)
  #v = math.pi * 2 * v                   # multiply by 2pi 
  v = "pi " + str(v)
  return v

def printResult(functions, axis, volume):
  result = "The volume of the solid formed by rotating the function {0} about the {1}-axis is: \nV = {2}"
  result = result.format(functions, axis, volume)
  print(bump + result + bump)

def setAxis():
  axis = input("on the axis: ")
  
  if axis in axes:
    return axis
  else:
    return "No axis given, exiting program."
    sys.exit(0)

# Defining the functions "f" and "g"
def setFunctions():
  function1 = input("The first function f: ")
  function2 = input("The second function g: ")
  return function1, function2 

# Defining the interval
def setInterval():
  upper_bound = input("from?: ")
  lower_bound = input("  to?: ") 
  return upper_bound, lower_bound

# Setting the differential variable to either x or y
# Note: Invert function g if function f is in terms of another axis
def setDifferential(functions):
  function1 = functions[0]
  function2 = functions[1]

  # Conditionals for functions "f" and "g"
  f1containsx = 'x' in function1.split() and 'y' not in function1.split()
  f1containsy = 'y' in function1.split() and 'x' not in function1.split()

  # Defining the independent variable
  if f1containsx or f1containsy:
    return 'x' if f1containsx else 'y'
  else:
    return "No variable given, exiting program."
    sys.exit(0)

if __name__ == "__main__":
  print(bump)
  
  # Setting the functions "f" and "g"
  functions = setFunctions()

  # Setting the differential variable to either x or y
  differential = Symbol(setDifferential(functions))

  # Sympify functions "f" and "g"
  functions = sympify(functions)

  # Setting the interval
  interval = setInterval()

  # Setting the axis of rotation
  axis = setAxis()

  # Determines whether functions are parallel or perpendicular to axis
  isParallel = str(axis) == str(differential) 

  # If parallel, use disc method. If perpendicular, use shell method.
  if isParallel:
    volume = discMethod(functions, differential, interval)    # <-- parallel
  else:
    volume = shellMethod(functions, differential, interval)   # <-- perpendicular

  # Print result
  printResult(functions, axis, volume)
