import matplotlib.pyplot as plt
from random import randint

from Environment import Environment
from Graph import Graph
from MazeGenerator import generate_maze
from Monitor import MazeMonitor


class Maze(Environment):

    def __init__(self, width, height, step_limit=100):
        self.__width = width
        self.__height = height

        self.__graph: Graph = None

        self.__initial_point = None
        self.__final_point = None

        self.__image: MazeMonitor = None

        self.__agent_position = None

        self.__counter = 0
        self.__step_limit = step_limit

        fig = plt.gca()

        x_axis = fig.axes.get_xaxis()
        x_axis.set_visible(False)

        y_axis = fig.axes.get_yaxis()
        y_axis.set_visible(False)

    def reset(self):
        self.__counter = 0
        self.__graph = generate_maze(self.__width, self.__height)

        self.__initial_point = randint(0, self.__height - 1)
        self.__final_point = randint(0, self.__height - 1)

        self.__agent_position = (1, self.__initial_point + 1)

        self.__image = MazeMonitor(self.__width, self.__height, self.__graph, self.__initial_point, self.__final_point)
        self.__image.build()

        return self.__image.image

    def __decode_action(self, action):
        x, y = self.__agent_position
        if action == 1:  # up
            y -= 1
        elif action == 2:  # down
            y += 1
        elif action == 3:  # left
            x -= 1
        elif action == 4:  # right
            x += 1

        return x, y

    def __is_valid(self, position):
        x, y = position

        return 1 <= x <= self.__width and 1 <= y <= self.__height

    def step(self, action):
        self.__counter += 1
        new_pos = self.__decode_action(action)

        done = False
        message = None

        if self.__counter < self.__step_limit:
            if not self.__graph.is_adjacent(new_pos, self.__agent_position) and self.__is_valid(new_pos):

                self.__image.move_agent((new_pos[0] - 1, new_pos[1] - 1))
                # print(new_pos, self.__agent_position)
                if new_pos == (self.__width, self.__final_point + 1):
                    reward = 100
                    done = True
                    message = "Agent successfully exited the maze! :)"
                else:
                    reward = -1

                self.__agent_position = new_pos
            else:
                reward = -2
        else:
            reward = -20
            done = True
            message = "Step limit reached :("

        return reward, self.__image.image, done, message

    def end(self):
        plt.show()

    def render(self):
        plt.imshow(self.__image.image)
        plt.pause(0.01)

    @property
    def image(self):
        return self.__image.image