from random import randint
from time import time

import matplotlib.pyplot as plt

from Maze import Maze

maze = Maze(20, 20, step_limit=20)
image, done = maze.reset(), False

tic = time()

while not done:
    maze.render()
    # print(maze.agent_position)
    action = randint(1, 4)
    # print(action)
    reward, observation, done, message = maze.step(action)

    print(reward)

toc = time()

print(toc - tic)

print(message)
