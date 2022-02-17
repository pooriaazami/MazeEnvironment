import numpy as np


class MatrixImage:
    def __init__(self, width, height, density=10, edge_density=2, initial_color=0):
        self.__width = width
        self.__height = height
        self.__edge_density = edge_density
        self.__density = density

        self.__image = np.ones((self.__width, self.__height, 3), dtype=np.float32) * initial_color

    @property
    def shape(self):
        return self.__width // self.__density, self.__height // self.__density

    def fill_rectangle(self, x, y, color):
        x_start = x * self.__density
        x_end = x_start + self.__density

        y_start = y * self.__density
        y_end = y_start + self.__density

        self.__image[y_start:y_end, x_start:x_end] = color

    def fill_upper_edge(self, x, y, color):
        x_start = x * self.__density
        x_end = x_start + self.__density

        y_start = y * self.__density
        y_end = y_start + self.__edge_density

        self.__image[y_start:y_end, x_start:x_end] = color

    def fill_lower_edge(self, x, y, color):
        x_start = x * self.__density
        x_end = x_start + self.__density

        y_start = (y + 1) * self.__density - self.__edge_density
        y_end = y_start + self.__edge_density

        self.__image[y_start:y_end, x_start:x_end] = color

    def fill_left_edge(self, x, y, color):
        x_start = x * self.__density
        x_end = x_start + self.__edge_density

        y_start = y * self.__density
        y_end = y_start + self.__density

        self.__image[y_start:y_end, x_start:x_end] = color

    def fill_right_edge(self, x, y, color):
        x_start = (x + 1) * self.__density - self.__edge_density
        x_end = x_start + self.__edge_density

        y_start = y * self.__density
        y_end = y_start + self.__density

        self.__image[y_start:y_end, x_start:x_end] = color

    def fill_center(self, x, y, color):
        x_start = x * self.__density + self.__edge_density
        x_end = x_start + self.__density - 2 * self.__edge_density

        y_start = y * self.__density + self.__edge_density
        y_end = y_start + self.__density - 2 * self.__edge_density

        self.__image[y_start:y_end, x_start:x_end] = color

    @property
    def image(self):
        return self.__image
