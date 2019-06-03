import numpy as np

import sys
np.set_printoptions(threshold=sys.maxsize)

h = 25
u, v, w = (8, 8, 20)

grid = np.zeros((u, v, w))

for i in range(u):
    for j in range(v):
        for k in range(w):
            x, y, z = 2 * i / u - 1, 2 * j / v - 1, h * k / w
            r = np.sqrt(x**2 + y**2)
            if z > 6:
                grid[i, j, k] = 1
                continue
            if z < 2: # height at which exhaust definitely ends
                grid[i, j, k] = 0
                continue

            if r > 0.8:
                grid[i, j, k] = 0

            dz = (6 - z) / 4 # 4 is the length of the exhaust
            grid[i, j, k] = np.clip(  (0.8 - r) / 0.8 * (z ** 0.2) , 0, 1)

with open('exhaust.pbrt', 'w') as f:
    f.write('''
MakeNamedMedium "exhaust"
  "rgb sigma_a" [ 0.030 0.030 0.030 ]
  "rgb sigma_s" [ 1 1 1 ]
  "string type" "heterogeneous"
  "integer nx" [ %d ]
  "integer ny" [ %d ]
  "integer nz" [ %d ]
  "point p0" [ -1 -1 4 ]
  "point p1" [  1  1 %d ]
  "float density" %s
''' % (u, v, w, h, np.array2string(grid.flatten('F'))))
