#!/usr/bin/env python3 

'''
Volume of Solids of Revolution Calculator
'''

from sympy import Integral, Symbol, sympify

import math
import sys

bump = "\n" + "-" * 50 + "\n"

# If the axis of rotation is perpendicular to f:
def discMethod(functions, x, interval):
  a = interval[0]
  b = interval[1]
  f = functions[0]
  g = functions[1]

  v = f ** 2 - g ** 2                   # square f
  v = Integral(v, (x, a, b)).doit()     # integrate f ** 2 - g ** 2
  v = math.pi * v                       # multiply by pi
  return v


# If the axis of rotation is parellel to f:
def cylinderMethod(functions, x, interval):
  a = interval[0]
  b = interval[1]
  f = functions[0]
  g = functions[1]

  v = x * (f - g)                       # multiply x by f
  v = Integral(v, (x, a, b)).doit()     # integrate x * (f - g)
  v = math.pi * 2 * v                   # multiply by 2pi 
  return v

# Determines the upper and lower bounds from f and g
def determineBounds(f):
  return None

# Determines the upper and lower function at a given interval
def determineUpperFunction(f, interval):
  return None

if __name__ == "__main__":
  print(bump)
  
  # Defining functions "f" and "g"
  function1 = input("The first function f: ")
  function2 = input("The second function g: ")

  # Conditionals for functions "f" and "g"
  f1containsx = 'x' in function1.split() and 'y' not in function1.split()
  f1containsy = 'y' in function1.split() and 'x' not in function1.split()
  f2containsx = 'x' in function2.split() and 'y' not in function2.split()
  f2containsy = 'y' in function2.split() and 'x' not in function2.split()

  # Defining the independent variable
  if f1containsx and f2containsx:
    variable = Symbol('x')
  elif f1containsy and f2containsy:
    variable = Symbol('y')
  else:
    print("No variable given, exiting program.")
    sys.exit(0)

  # Sympify functions "f" and "g"
  function1 = sympify(function1)
  function2 = sympify(function2)

  # Create list of functions
  functions = [function1, function2]

  # Defining the interval
  upper_bound = input("from?: ")
  lower_bound = input("  to?: ")
  interval = [upper_bound, lower_bound]

    


  # Defining the axis of rotation
  axis = input("on the axis: ")

  # Determines whether functions are parallel or perpendicular to axis
  if axis == variable:
    volume = discMethod(functions, variable, interval)    # <-- parallel
  elif axis != variable:
    volume = shellMethod(functions, variable, interval)   # <-- perpendicular
  else:
    print("No axis given, exiting program.")
    sys.exit(0)


  # Print result
  print(bump)
  result = "The volume of the solid formed by rotating the function {0} about the {1}-axis is: \nV = {2}"
  result = result.format(functions, axis, volume)
  print(result)
  print(bump)
