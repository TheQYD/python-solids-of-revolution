#!/usr/bin/env python3 

'''
Volume of Solids of Revolution Calculator
'''

from sympy import Integral, Symbol, sympify

import math

# If the axis of rotation is perpendicular to f:
def discVolume(f, x):
  v = f ** 2                    # square f(x)
  v = Integral(v, x).doit()     # integrate f(x) ** 2
  v = math.pi * v
  return v


# If the axis of rotation is parellel to f:
def cylinderVolume(f):
  return None

if __name__ == "__main__":
  x = Symbol('x')

  f = input("f(x) = ")
  f = sympify(f)
  print(f)

  volume = discVolume(f, x)
  print(volume)
