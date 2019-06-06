import numpy as np

import sys
np.set_printoptions(threshold=sys.maxsize)

h = 10
u, v, w = (10, 10, 10)

grid = np.zeros((u, v, w))
colors = np.zeros((3, u, v, w))

baseColor = (50, 30, 0)
endColor = (50, 0, 30)

def setColor(i,j,k, color):
    for n in range(3):
        colors[n,i,j,k] = color[n]

for i in range(u):
    for j in range(v):
        for k in range(w):
            x, y, z = 2 * i / u - 1, 2 * j / v - 1, h * k / w
            r = np.sqrt(x**2 + y**2)*100

            grid[i,j,k] = 1.0 - (k/float(w))**2
            color = [0,0,0]
            for n in range(3):
                color[n] = baseColor[n]*(1-(k/float(w))**2) + endColor[n]*(k/float(w))**2
            setColor(i,j,k,color)
            continue
            
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
MakeNamedMedium "flame"
  "rgb sigma_a" [ 2.5 2.5 2.5 ]
  "rgb sigma_s" [ 0.0 0.0 0.0 ]
  "string type" "emissive"
  "integer nx" [ %d ]
  "integer ny" [ %d ]
  "integer nz" [ %d ]
  "point p0" [ -1 -1 -1 ]
  "point p1" [ 1 1 1 ]
  "float density" %s
  "float Le" %s
''' % (u, v, w, np.array2string(grid.flatten('F')), np.array2string(colors.flatten('F'))))
