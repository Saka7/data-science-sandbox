from math import sqrt, pow
import random

import pants as ants
import matplotlib.pyplot as plt
import numpy as np

euclidean = lambda a, b: sqrt(pow(a[1] - b[1], 2) + pow(a[0] - b[0], 2))
nodes = [[random.uniform(0, 10), random.uniform(0, 10)] for _ in range(10)]

world = ants.World(nodes, euclidean)
acoSolver = ants.Solver()

solution = acoSolver.solve(world)

plt.style.use('ggplot')
coords = np.array(nodes)
plt.plot(coords[:,0], coords[:,1], 'r.')
plt.xticks(np.arange(0, 11, 1.0))
plt.yticks(np.arange(1, 11, 1.0))
plt.ylabel('y')
plt.xlabel('x')
plt.show()

tcoords = np.array(solution.tour)
plt.plot(coords[:,0], coords[:,1], 'r.')
plt.plot(tcoords[:,0], tcoords[:,1], 'b')
plt.xticks(np.arange(0, 11, 1.0))
plt.yticks(np.arange(1, 11, 1.0))
plt.ylabel('y')
plt.xlabel('x')
plt.show()

