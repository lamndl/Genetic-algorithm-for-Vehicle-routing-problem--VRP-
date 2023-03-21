import random
import math
import pickle
from typing import List
from settings import VERTICES_NUM

Point = tuple[int, int]

vertices: List[Point] = [(0, 0)]
distance_matrix: List[List[float]] = []


def generate_vertices():
    for i in range(VERTICES_NUM):
        vertices.append((random.randint(-50, 50), random.randint(-50, 50)))
    for i in vertices:
        distance_matrix.append([math.dist(i, j) for j in vertices])


generate_vertices()
with open('vertices', 'wb') as fp:
    pickle.dump(vertices, fp)

with open('distance', 'wb') as fp:
    pickle.dump(distance_matrix, fp)
