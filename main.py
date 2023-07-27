#!/usr/bin/env python3 

'''
Volume of Solids of Revolution Calculator
'''

from sympy import Integral, Symbol, sympify

import math
import sys

axes = ('x', 'y')
bump = "\n" + "-" * 80 + "\n"

# If the axis of rotation is perpendicular to the functions:
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


# If the axis of rotation is parellel to the functions:
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

# Determines the upper and lower bounds from f and g
def determineBounds(f):
  return None

# Determines what variable the function f is in terms of
# Note: Invert function g if function f is in terms of another axis
def parseFunctionVariables(functions):
  function1 = functions[0]
  function2 = functions[1]

  # Conditionals for functions "f" and "g"
  f1containsx = 'x' in function1.split() and 'y' not in function1.split()
  f1containsy = 'y' in function1.split() and 'x' not in function1.split()

  # Defining the independent variable
  if f1containsx or f1containsy:
    return 'x' if f1containsx else 'y'
  else:
    print("No variable given, exiting program.")
    sys.exit(0)

if __name__ == "__main__":
  print(bump)
  
  # Defining functions "f" and "g"
  function1 = input("The first function f: ")
  function2 = input("The second function g: ")
  functions = [function1, function2]

  variable = Symbol(parseFunctionVariables(functions))

  # Sympify functions "f" and "g"
  functions[0] = sympify(functions[0])
  functions[1] = sympify(functions[1])

  # Create list of functions
  #functions = [function1, function2]

  # Defining the interval
  upper_bound = input("from?: ")
  lower_bound = input("  to?: ")
  interval = [upper_bound, lower_bound]


  # Defining the axis of rotation
  axis = input("on the axis: ")

  # Checking if axis is x or y
  if axis in axes:
    isParallel = str(axis) == str(variable)
    isPerpendicular = str(axis) != str(variable)
  else:
    print("No axis given, exiting program.")
    sys.exit(0)

  # Determines whether functions are parallel or perpendicular to axis
  if isParallel:
    print("DISC!")
    volume = discMethod(functions, variable, interval)    # <-- parallel
  elif isPerpendicular:
    print("SHELL!")
    volume = shellMethod(functions, variable, interval)   # <-- perpendicular

  # Print result
  print(bump)
  result = "The volume of the solid formed by rotating the function {0} about the {1}-axis is: \nV = {2}"
  result = result.format(functions, axis, volume)
  print(result)
  print(bump)
