import numpy as np
from PIL import Image


def find_vector(point1: tuple[int, int], point2: tuple[int, int]) -> tuple[int, float] | tuple[int, int]:
    if point1[0] == point2[0]:
        return 0, 1
    return 1, (point2[1] - point1[1])/(point2[0] - point1[0])


def draw_line(point1: tuple, point2: tuple, image: None, color: tuple = (0, 0, 0)):
    vector = find_vector(point1, point2)
    position = list(point1)
    end = list(point2)

    if vector[0] == 0:
        for i in range(point2[1] - point1[1]):
            image[position[0], int(position[1])] = color
            position += vector

    elif vector[1] == 0:
        for i in range(point2[0] - point1[0]):
            image[position[0], int(position[1])] = color
            position += vector

    else:
        for i in range(point2[0] - point1[0]):
            image[position[0], int(position[1])] = color
            if int(position[1]) != int(position[1] + vector[1]):
                image[position[0] + 1, position[1]] = (128, 128, 128)
            position += vector


img = Image.new("RGB", (256, 256), "white")
pixels = img.load()
draw_line((0, 0), (128, 128), pixels)
img.show()
