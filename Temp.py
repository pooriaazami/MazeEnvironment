from random import randint

import matplotlib.pyplot as plt

# width = 30
# height = 30
# maze = generate_maze(width, height)
# maze.show()
#
# monitor = MazeMonitor(width, height, graph=maze)
# monitor.build()
#
# image = monitor.image
from Maze import Maze

maze = Maze(20, 20)
image, done = maze.reset(), False

while not done:
    maze.render()
    action = randint(1, 4)
    print(action)
    reward, observation, done, message = maze.step(action)

print(message)
