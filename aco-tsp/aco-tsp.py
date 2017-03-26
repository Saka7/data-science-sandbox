from math import sqrt, pow
import random

import pants as ants
import matplotlib.pyplot as plt
import numpy as np

def euclidean(a, b):
  return sqrt(pow(a[1] - b[1], 2) + pow(a[0] - b[0], 2))

def generate_nodes(min, max, amount):
  return [[random.uniform(min, max), random.uniform(min, max)] for _ in range(amount)]

def find_shortest_path(coordinates, function):
  print(ants)
  world = ants.World(coordinates, function)
  acoSolver = ants.Solver()
  return acoSolver.solve(world)

def draw_nodes(nodes):
  plt.style.use('ggplot')
  coordinates = np.array(nodes)
  plt.plot(coordinates[:,0], coordinates[:,1], 'r.')
  plt.xticks(np.arange(0, 11, 1.0))
  plt.yticks(np.arange(1, 11, 1.0))
  plt.ylabel('y')
  plt.xlabel('x')
  plt.show()

def draw_shortest_path(nodes, solution):
  coordinates = np.array(nodes)
  shortest_path_coordinates = np.array(solution.tour)
  starting_point = coordinates[solution.start]
  plt.plot(starting_point[0], starting_point[1], 'go')
  plt.plot(coordinates[:,0], coordinates[:,1], 'r.')
  plt.plot(shortest_path_coordinates[:,0], shortest_path_coordinates[:,1], 'b')
  plt.xticks(np.arange(0, 11, 1.0))
  plt.yticks(np.arange(1, 11, 1.0))
  plt.ylabel('y')
  plt.xlabel('x')
  plt.show()

if __name__ == "__main__":
  nodes = generate_nodes(0, 10, 10)
  draw_nodes(nodes)
  shortest_path = find_shortest_path(nodes, euclidean)
  draw_shortest_path(nodes, shortest_path)
  print("starting point = ", shortest_path.start)
  print("distance = ", shortest_path.distance)
  print("path = ", shortest_path.tour)
