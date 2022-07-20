import math

from examples.shared import up, down

def target(x, y):  
  p = 1.4 - 5.8*x + 10.7*x**2 - 5.7*x**3

  g1 = 0.75*math.exp(-0.25*(9*x - 2)**2 - 0.25*(9*y - 2)**2) + 0.75*math.exp(-(9*x + 1)**2/49 - (9*y + 1)/10) + \
      0.5*math.exp(-0.25*(9*x-7)**2 - 0.25*(9*y - 3)**2) - 0.2*math.exp(-(9*x-4)**2 - (9*y-7)**2) 
  
  g2 = 0

  if x > 0.15 and x < 0.85 and y > 0.3 and y < 0.9 and y > p:
    g2 = -math.exp(2 + 0.35**2 / ((x - 0.5)**2 - 0.35**2) + 0.3**2 / ((y - 0.6)**2 - 0.3**2))

  return g1 * (g2 + 1.1 - x)

def graph(x, y, ri):
  p = 1.4 - 5.8*x + 10.7*x**2 - 5.7*x**3

  if x > 0.15 and x <= 0.55 and y > p:
    return ri * up(0.15, 0.45, x)

  if x > 0.55 and x < 0.85 and y > p:
    return ri * down(0.55, 0.85, x)

  return 0
