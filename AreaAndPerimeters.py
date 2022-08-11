import math


def PerimeterOfRectangle(g,y):
  return 2*(g+y)
print(PerimeterOfRectangle(3,4))

def AreaOfRectangle(g,y):
  return g*y
print(AreaOfRectangle(3,4))

def AreaOfRightTriangle(a,b):
  return a*b /2
print(AreaOfRightTriangle(4,5))

def PerimeterOfRightTriangle(a,b,h):
  return a + b + h
print(PerimeterOfRightTriangle(2,8,7))

def AreaOfParallelogram(b,h):
  return b*h
print(AreaOfParallelogram(7,3))

def PerimeterOfParallelogram(a,b):
  return 2*a + 2*b
print(PerimeterOfParallelogram(6,2))

def PerimeterOfSquare(a):
  return 4*a
print(PerimeterOfSquare(6))

def AreaOfSquare(a):
  return a*a
print(AreaOfSquare(6))

def AreaOfCircle(r):
  return r*r*math.pi
print(AreaOfSquare(3))

def PerimeterOfCircle(r):
  return 2*r*math.pi
print(PerimeterOfCircle(5))

def AreaOfEquilateralTriangle(a):
  return math.sqrt(3)/4 * (a*a)
print(AreaOfEquilateralTriangle(7))

def PerimeterOfEquilateralTriangle(a):
  return 3*a
print(PerimeterOfEquilateralTriangle(9))

def AreaOfSphere(r):
  return 4*math.pi*r*r
print(AreaOfSphere(2))

def VolumeOfSphere(r):
  return 4/3*math.pi*r*r*r
print(VolumeOfSphere(8))





