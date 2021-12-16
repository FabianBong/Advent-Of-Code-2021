from functools import reduce

import numpy as np


def is_valid(x, y, n):
    if x >= 0 and y >= 0 and x < n and y < n:
        return True
    return False

def lowest_risk_path(grid):
    n = len(grid)
    risks = np.ones_like(grid) * float('inf')

    node = (0, 0)  # start
    not_visited = {node}
    risks[node] = 0
    while node != (n - 1, n - 1):  # to end
        x, y = node
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            xdx, ydy = x + dx, y + dy
            if not (0 <= xdx < n and 0 <= ydy < n):
                continue
            if risks[xdx, ydy] == float('inf'):
                not_visited.add((xdx, ydy))
            risks[xdx, ydy] = min(risks[node] + grid[xdx, ydy], risks[xdx, ydy])
        not_visited.remove(node)
        node = reduce(lambda a, b: a if risks[a] < risks[b] else b, not_visited)

    return risks[node]


def generate_cave(chitons, n):
    grid2 = np.tile(np.array(chitons), (5, 5))
    for i in range(5):
        for j in range(5):
            if i == j == 0:
                continue
            tile = grid2[i * n:(i + 1) * n, j * n:(j + 1) * n]
            tile += i + j
            tile %= 10
            tile[tile < i + j + 1] += 1

    return grid2


chitons = []
with open("/Users/fabianbong/Documents/Advent_Of_Code/Day_15/input.txt") as f:
    for line in f.readlines():
        chitons.append([int(i) for i in line.strip('\n')])

print(lowest_risk_path(np.array(chitons)))
