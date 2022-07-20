def h0(t):
  return (1 + 3*t + 6*t **2) * (1 - t) ** 3

def h1(t):
  return t ** 3 * (10 - 15*t + 6*t ** 2)

def down(a1, a2, t):
  if t < a1:
    return 1
  
  if t >= a1 and t <= a2:
    return h0((t - a1) / (a2 - a1))

  return 0

def up(a1, a2, t):
  if t < a1:
    return 0

  if t >= a1 and t <= a2:
    return h1((t - a1) / (a2 - a1))

  return 1
