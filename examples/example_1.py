import math

def target(x, y):  
  if (x - 0.5)**2 + (y - 0.5)**2 < 0.16:
    return (1 + int(3.5 * math.sqrt(x*x + y*y)))*math.sin(math.pi * x)*math.sin(math.pi * y)

  return 0

def graph(x, y, ri):
  if x ** 2 + y ** 2 <= 16/49 and (x - 0.5) ** 2 + (y - 0.5) ** 2 <= 0.16:
    return ri
  
  if x ** 2 + y ** 2 > 16/49 and x ** 2 + y ** 2 <= 36/49 and (x - 0.5) ** 2 + (y - 0.5) ** 2 <= 0.16:
    return -ri
  
  if x ** 2 + y ** 2 > 36/49 and (x - 0.5) ** 2 + (y - 0.5) ** 2 <= 0.16:
    return ri

  return 0
