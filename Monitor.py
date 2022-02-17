# fig = plt.gca()
#
# x_axis = fig.axes.get_xaxis()
# x_axis.set_visible(False)
#
# y_axis = fig.axes.get_yaxis()
# y_axis.set_visible(False)
import numpy as np

from MatrixImage import MatrixImage


class MazeMonitor:
    def __init__(self, width, height, graph, start, end, **kwargs):
        self.__wall_color = kwargs.get('wall_color', 0)
        self.__background_color = kwargs.get('background', 1)

        self.__image = MatrixImage(width * 10, height * 10, initial_color=self.__background_color)
        self.__graph = graph

        self.__width = width
        self.__height = height

        self.__start = start
        self.__end = end

        self.__agent_location = (0, self.__start)

        self.__agent_color = np.array([0, 1, 0])

    def __build_edges(self):
        for x in range(self.__width):
            self.__image.fill_upper_edge(x, 0, self.__wall_color)
            self.__image.fill_lower_edge(x, self.__height - 1, self.__wall_color)
            self.__image.fill_left_edge(0, x, color=self.__wall_color)
            self.__image.fill_right_edge(self.__width - 1, x, color=self.__wall_color)

    def __draw_graph_edge(self, edge):
        first, second = edge

        first_x, first_y = first
        second_x, second_y = second

        first_x -= 1
        first_y -= 1
        second_x -= 1
        second_y -= 1

        if first_x == second_x:  # vertical line
            upper, lower = (first_y, second_y) if first_y > second_y else (second_y, first_y)

            self.__image.fill_upper_edge(first_x, upper, self.__wall_color)
            self.__image.fill_lower_edge(first_x, lower, self.__wall_color)
        else:  # horizontal line
            upper, lower = (first_x, second_x) if first_x > second_x else (second_x, first_x)

            self.__image.fill_left_edge(upper, first_y, self.__wall_color)
            self.__image.fill_right_edge(lower, first_y, self.__wall_color)

    def build(self):
        self.__build_edges()

        for edge in self.__graph.edges:
            self.__draw_graph_edge(edge)

        self.__image.fill_left_edge(0, self.__start, self.__background_color)
        self.__image.fill_right_edge(self.__width - 1, self.__end, self.__background_color)

        self.__image.fill_center(*self.__agent_location, self.__agent_color)

    def move_agent(self, location):
        self.__image.fill_center(*self.__agent_location, self.__background_color)
        self.__agent_location = location

        self.__image.fill_center(*self.__agent_location, self.__agent_color)

    @property
    def image(self):
        return self.__image.image
