import numpy as np
import random as rand
import matplotlib.pyplot as plt

def fitness(x, y):
  return 100 * ((y - (x**2))**2) + ((1 - (x**2))**2)

def vector_velocity(number_of_participles, a, pbest, gbest, v):
  for i in range(number_of_participles):
    v[0][i] = 0.7 * v[0][i] + (pbest[0][i] - a[0][i]) * rand.random() * 1.47 + (gbest[0][0] - a[0][i]) * rand.random() * 1.47
    a[0][i] = a[0][i] + v[0][i]
    v[1][i] = 0.7 * v[1][i] + (pbest[1][i] - a[1][i]) * rand.random() * 1.47 + (gbest[0][1] - a[1][i]) * rand.random() * 1.47
    a[1][i] = a[1][i] + v[1][i]

if __name__ == '__main__':
  number_of_participles = 100
  num_variables = 2
  max_iteration = 500

  a = np.empty((num_variables, number_of_participles))
  v = np.empty((num_variables, number_of_participles))
  pbest = np.empty((num_variables, number_of_participles))
  gbest = np.empty((1, 2))
  r = np.empty((number_of_participles))

  for i in range(0, num_variables):
    for j in range(0, number_of_participles):
      pbest[i][j] = rand.randint(-20, 20)
      a[i][j] = pbest[i][j]
      v[i][j] = 0
  
  for i in range(0, number_of_participles):
    r[i] = fitness(a[0][i], a[1][i])

  pbest = np.sort(pbest)
  r = np.sort(r)

  gbest[0][0] = pbest[0][0]
  gbest[0][1] = pbest[1][0]

  plt.ion()
  plt.style.use('ggplot')
  fig = plt.figure()
  plot = fig.add_subplot(111)
  range_values = np.arange(-10.0, 10.0, 0.01)

  for iteration in range(max_iteration):
    for i in range(number_of_participles):
      if(fitness(a[0][i], a[1][i]) < fitness(pbest[0][i], pbest[1][i])):
        pbest[0][i] = a[0][i]
        pbest[1][i] = a[1][i]
      if(fitness(pbest[0][i], pbest[1][i]) < fitness(gbest[0][0], gbest[0][1])):
        gbest[0][0] = pbest[0][i]
        gbest[0][1] = pbest[1][i]
      vector_velocity(number_of_participles, a, pbest, gbest, v)
    print('iteration: ' + str(iteration) + ' - gbest: ' +str(gbest))

    plot.plot(a[0], a[1], 'rx')
    plot.plot(gbest[0][0], gbest[0][1], "bo")
    plot.plot(range_values, fitness(range_values, range_values), color="green")
    plot.set_xlim(-10, 10)
    plot.set_ylim(-10, 10)
    plot.set_title('PSO gbest')

    fig.canvas.draw()
    plot.clear()
