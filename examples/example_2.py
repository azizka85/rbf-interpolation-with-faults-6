import math

from examples.shared import down

def target(x, y):  
  p = 0.5 + 0.2 * math.sin(5 * math.pi * x / 3)
  g = math.pi * ((x - 0.2) ** 2 + (y - 0.7) ** 2) / 1.3

  if g <= math.pi / 2 and y > p:
    return 0.5 * math.cos(g) ** 4
  
  if g <= math.pi / 2 and y <= p:
    return 0.25 * (1 - x) ** 2 * math.cos(g) ** 2

  return 0

def graph(x, y, ri):
  p = 0.5 + 0.2 * math.sin(5 * math.pi * x / 3)

  if x < 0.9 and y > p:
    return ri * down(0.5, 0.9, x)

  return 0
