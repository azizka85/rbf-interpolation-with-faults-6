import math
from time import time

import numpy as np

import matplotlib.pyplot as plt

import funcs

x = np.outer(np.linspace(-1, 1, 101), np.ones(101))
y = np.outer(np.linspace(-1, 1, 101), np.ones(101)).T

n, m = x.shape

z = np.zeros(x.shape)

for i in range(0, n):
  for j in range(0, m):
    z[i, j] = funcs.target(x[i, j], y[i, j])

max_az = np.max(np.absolute(z))

fig = plt.figure()

n = 128
n_min = 2

ri = 0.8 # 8 * math.sqrt(n_min / n)

points = np.random.normal(0, 1, (n, 2))

points = np.array([np.array([p[0], p[1], funcs.graph(p[0], p[1], ri)]) for p in points])

plt.title(f'RBF VS CS-RBF, n={n}, n_min={n_min}')

ax = fig.add_subplot(1, 4, 1)
ax.set_xticks(np.arange(-1, 1.1, 0.4))
ax.set_yticks(np.arange(-1, 1.1, 0.2))
ax.scatter(points[:, 0], points[:, 1])
ax.grid()
ax.set_title('Scatter plot')

ax = fig.add_subplot(1, 4, 2, projection='3d')
ax.plot_surface(x, y, z,cmap='plasma')
ax.set_title('Surface plot')

start = time()
print('rbf start: ', start)

b = funcs.rbf(points)
z_rbf = funcs.rbf_interpolant(b, points, x, y, ri)
mre = np.max(np.absolute(z-z_rbf)) / max_az

finish = time()
print('rbf finish: ', finish, ', time: ', finish - start)

ax = fig.add_subplot(1, 4, 3, projection='3d')
ax.plot_surface(x, y, z_rbf, cmap='plasma')
ax.set_title(f'Without Faults, mre={round(mre, 2)}, time={round(finish - start, 2)}')

start = time()
print('cs rbf start: ', start)

new_points, new_tree, ri, b = funcs.cs_rbf(points, ri, n_min)
z_cs_rbf = funcs.cs_rbf_interpolant(new_tree, b[0], new_points, x, y, ri)
mre = np.max(np.absolute(z-z_cs_rbf)) / max_az

finish = time()
print('cs rbf finish: ', finish, ', time: ', finish - start)

ax = fig.add_subplot(1, 4, 4, projection='3d')
ax.plot_surface(x, y, z_cs_rbf, cmap='plasma')
ax.set_title(f'With Faults, mre={round(mre, 2)}, time={round(finish - start, 2)}')

plt.show()
