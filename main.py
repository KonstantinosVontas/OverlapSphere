import csv
from random import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

import numpy as np
import overlap
from scipy.spatial import ConvexHull

f = open('myData.csv', 'w')

for i in range(1):
    writer = csv.writer(f)

    vertices = np.array([
        [-1, -1, -1],  # 1
        [1, -1, -1],  # 2
        [1, 1, -1],  # 3
        [-1, 1, -1],  # 4
        [-1, -1, 1],  # 5
        [1, -1, 1],  # 6
        [1, 1, 1],  # 7
        [-1, 1, 1]  # 8
    ])
    hex = overlap.Hexahedron(vertices)

    radius = np.random.uniform(1, 1)  # range of sphere size
    axis_x = 0
    axis_y = 0
    axis_z = 0

    sphere = overlap.Sphere((axis_x, axis_y, axis_z), radius)

    volHex = ConvexHull(vertices).volume  # since we have a cube vol_hex = a**3
    volSphere = 4 / 3 * np.pi * radius ** 3

    # vapour fraction = alpha
    alpha = volSphere / volHex

    result = overlap.overlap(sphere, hex)
    print(result)
    writer.writerow([result])

    print("The vapour fraction is : ", alpha)

f.close()


# code for plotting the cube and the sphere.

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
r = [-1, 1]
X, Y = np.meshgrid(r, r)
one = np.ones(4).reshape(2, 2)
ax.plot_surface(X, Y, one, alpha=0.5)
ax.plot_surface(X, Y, -one, alpha=0.5)
ax.plot_surface(X, -one, Y, alpha=0.5)
ax.plot_surface(X, one, Y, alpha=0.5)
ax.plot_surface(one, X, Y, alpha=0.5)
ax.plot_surface(-one, X, Y, alpha=0.5)
ax.scatter3D(vertices[:, 0], vertices[:, 1], vertices[:, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')




u = np.linspace(0, 2 * np.pi, 100)  # φ
v = np.linspace(0, np.pi, 100)  # θ

x = radius * np.outer(np.cos(u), np.sin(v)) + axis_x
y = radius * np.outer(np.sin(u), np.sin(v)) + axis_y
z = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + axis_z

ax.plot_wireframe(x, y, z, rstride=3, cstride=3)

plt.show()
