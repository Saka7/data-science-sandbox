from math import sqrt, pow
import random

import pants as ants
import matplotlib.pyplot as plt
import numpy as np

def euclidean_plane(a, b):
  """ The two-dimensional Euclidean plane """
  return sqrt(pow(a[1] - b[1], 2) + pow(a[0] - b[0], 2))

def generate_coordinates(min, max, amount):
  """
    Generates 2D array of random coordinates (x, y)

    :param min: minimum possible value
    :param max: maximum possible value
    :param amount: amount of rows (pairs of coordinates)
    :return: array of generated coordinates
  """
  return [[random.uniform(min, max), random.uniform(min, max)] for _ in range(amount)]

def find_shortest_path(coordinates, function):
  """
    Finds shortest path using Ant Colony Optimization Algorithm

    :param coordinates: coordinates of nodes which should be visited
    :param function: plane function
    :return: coordinates of shortest path
  """
  return ants.Solver().solve(ants.World(coordinates, function))

def draw_nodes(nodes_plot, nodes):
  """
    Draws nodes as a dots-chart

    :param nodes_plot: subplot on which chart should be drawn
    :param nodes: (x, y) coordinates of each node
    :return: nothing
  """
  coordinates = np.array(nodes)
  nodes_plot.plot(coordinates[:,0], coordinates[:,1], 'r.')
  nodes_plot.set_title('Path nodes')

def draw_shortest_path(shortest_path_plot, nodes, solution):
  """
    Draws shortest path as a line chart
    
    :param nodes_plot: subplot on which chart should be drawn
    :param nodes: (x, y) coordinates of each node which should be visited
    :param solution: shortest path
    :return: nothing
  """
  coordinates = np.array(nodes)
  shortest_path_coordinates = np.array(solution.tour)
  starting_point = coordinates[solution.start]
  shortest_path_plot.plot(starting_point[0], starting_point[1], 'go')
  shortest_path_plot.plot(coordinates[:,0], coordinates[:,1], 'r.')
  shortest_path_plot.plot(shortest_path_coordinates[:,0], shortest_path_coordinates[:,1], 'b')
  shortest_path_plot.set_title('Shortest path')

if __name__ == "__main__":
  # Generating 2x10 array of random values from 0 to 10 
  nodes = generate_coordinates(0, 10, 10)
  # Change matplotlib styling
  plt.style.use('ggplot')
  # Creating two subplot: one for nodes and one for shortest path
  f, (nodes_plot, shortest_path_plot) = plt.subplots(1, 2, sharey=True, sharex=True)
  # Drawing nodes dot-chart
  draw_nodes(nodes_plot, nodes)
  # Calculating shortest path
  shortest_path = find_shortest_path(nodes, euclidean_plane)
  # Drawing shortest path line chart
  draw_shortest_path(shortest_path_plot, nodes, shortest_path)

  # Configuring matplotlib
  plt.xticks(np.arange(0, 11, 1.0))
  plt.yticks(np.arange(1, 11, 1.0))
  plt.ylabel('y')
  plt.xlabel('x')
  plt.show()

  print("starting point = ", shortest_path.start)
  print("distance = ", shortest_path.distance)
  print("path = ", shortest_path.tour)
