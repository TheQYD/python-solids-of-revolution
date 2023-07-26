#!/usr/bin/env python3 

'''
Volume of Solids of Revolution Calculator
'''

from sympy import Integral, Symbol, sympify

import math

# If the axis of rotation is perpendicular to f:
def discVolume(f, x, a, b):
  v = f ** 2                    # square f(x)
  v = Integral(v, x).doit()     # integrate f(x) ** 2
  v = sympy.pi * v              # multiply by pi
  return v


# If the axis of rotation is parellel to f:
def cylinderVolume(f):
  return None

if __name__ == "__main__":
  x = Symbol('x')

  # The function "f"
  f = input("f(x) = ")
  f = sympify(f)
  
  # The bounds [a, b]
  a = input("from? ")
  b = input("to? ")

  v = discVolume(f, x, a, b)
  
  result = "The volume of the solid formed by rotating the function {0} about the {1} is: \n V = {3}"
  result = result.format(f, 'x-axis', v)
  print(result)
