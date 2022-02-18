from random import randint
from time import time

from tqdm import tqdm

import matplotlib.pyplot as plt

from Maze import Maze

maze = Maze(20, 20, step_limit=1000000)
image, done = maze.reset(), False

tic = time()

avg = 0

for _ in tqdm(range(100)):
    counter = 0
    done = False
    while not done:
        # maze.render()
        # print(maze.agent_position)
        action = randint(1, 4)
        # print(action)
        reward, observation, done, message = maze.step(action)
        counter += 1
    maze.reset()
    avg += counter
    print(counter)

    # print(reward)
print(avg / 100)
print(message)
