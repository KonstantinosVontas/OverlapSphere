import csv
from random import random

import numpy as np
import overlap
from scipy.spatial import ConvexHull

f = open('myData.csv', 'w')

for i in range(200000):
    writer = csv.writer(f)

    vertices = np.array((
        (-1, -1, -1),  # 1
        (1, -1, -1),  # 2
        (1, 1, -1),  # 3
        (-1, 1, -1),  # 4
        (-1, -1, 1),  # 5
        (1, -1, 1),  # 6
        (1, 1, 1),  # 7
        (-1, 1, 1)  # 8
    ))
    hex = overlap.Hexahedron(vertices)




    rad = np.random.uniform(0.1, 1.2406999)  # range of sphere size
    sphere = overlap.Sphere((0, 0, 1), rad)

    volHex = ConvexHull(vertices).volume # since we have a cube vol_hex = a**3
    volSphere = 4 / 3 * np.pi * rad ** 3

    #vapour fraction = alpha
    alpha = volSphere/volHex

    result = overlap.overlap(sphere, hex)
    print(result)
    writer.writerow([result])

    print("The vapour fraction is : ", alpha)

f.close()
