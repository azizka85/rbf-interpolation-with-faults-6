import math
from time import time

import numpy as np

from scipy.spatial import KDTree
from scipy.sparse.linalg import LinearOperator, cg

from examples.example_3 import target, graph

def distance(p1, p2):
  return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2)

def basis(r, a = 1.):
  return (4 * r / a + 1) * (1 - r / a) ** 4

def rbf(points):
  m = len(points)

  A = np.zeros((m, m))
  f = np.zeros(m)

  for i in range(0, m):
    f[i] = target(points[i][0], points[i][1])

    for j in range(0, m):
      p1 = points[i]
      p2 = points[j]

      r = distance(
        [p1[0], p1[1], 0], 
        [p2[0], p2[1], 0]
      )

      A[i][j] = basis(r)

  return np.linalg.solve(A, f)

def rbf_interpolant(b, points, x, y, ri):
  m = len(points)
  n = x.shape[0]

  z = np.zeros(x.shape)
  
  for k in range(0, m):
    for i in range(0, n):
      for j in range(0, n):
        r = distance(
          (x[i, j], y[i, j], 0), 
          [points[k][0], points[k][1], 0]
        )

        z[i, j] += b[k] * basis(r)

  return z

def cs_rbf(points, ri, n_min):
  n = len(points)

  tree = KDTree(points, copy_data=True)

  res = []
  fb = []

  max_count = 0
  min_count = n

  new_points = []

  for p in points:    
    count = tree.query_ball_point(p, ri, return_length=True)

    if count >= n_min:
      max_count = max(max_count, count)
      min_count = min(min_count, count)

      new_points.append(p)

  n = len(new_points)

  print(f'points = {n}, max count = {max_count}, min count = {min_count}, ri = {ri}')

  new_tree = KDTree(new_points, copy_data=True)

  for p in new_points:
    fb.append(target(p[0], p[1]))
    
    found = new_tree.query_ball_point(p, ri)

    res.append([[i, basis(distance(p, new_points[i]), ri)] for i in found])

  def mv(v):
    f = np.zeros(n)

    for i in range(n):
      for item in res[i]:
        f[i] += item[1] * v[item[0]]

    return f

  A = LinearOperator((n, n), matvec=mv)

  start = time()

  b = cg(A, fb)

  finish  =  time()

  print(f'time = {finish - start}, iterations={b[1]}')

  return new_points, new_tree, ri, b

def cs_rbf_interpolant(tree: KDTree, b, points, x, y, ri):
  n, m = x.shape

  z = np.zeros(x.shape)

  for i in range(0, n):
    for j in range(0, m):
      found = tree.query_ball_point([x[i, j], y[i, j], graph(x[i, j], y[i, j], ri)], ri)    

      for k in found:        
        p = points[k]
        z[i, j] += b[k] * basis(distance((x[i, j], y[i, j], graph(x[i, j], y[i, j], ri)), p), ri)

  return z  
