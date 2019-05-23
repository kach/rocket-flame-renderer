import numpy as np

import sys
np.set_printoptions(threshold=sys.maxsize)

u, v = (10, 10)

grid = np.zeros((u, v))

for i in range(u):
    for j in range(v):
        if i == 0 or i == u - 1 or j == 0 or j == v - 1:
            grid[i, j] = 0
            continue
        x, y = i / u - 0.5, j / v - 0.5
        grid[i, j] = np.exp(-np.power(np.sqrt(x**2 + y**2), 2.) / (0.05 * np.power(1, 2.))) + np.random.random() / 3

with open('hill.pbrt', 'w') as f:
    f.write('''
ObjectBegin "hill1"
  Shape "heightfield"
    "integer nu" %d
    "integer nv" %d
    "float Pz" %s
ObjectEnd
''' % (u, v, np.array2string(np.ndarray.flatten(grid))))
