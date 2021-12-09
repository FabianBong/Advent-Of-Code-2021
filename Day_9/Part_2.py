from collections import deque as queue
from functools import reduce

with open("/Users/fabianbong/Documents/Advent_Of_Code/Day_9/input.txt") as f:
    lines = f.readlines()

lowPoints = []

for i in range(0, 100):
    for j in range(0, 100):
        if j - 1 >= 0:
            if int(lines[i][j - 1]) <= int(lines[i][j]):
                continue
        if j + 1 < 100:
            if int(lines[i][j + 1]) <= int(lines[i][j]):
                continue
        if i - 1 >= 0:
            if int(lines[i - 1][j]) <= int(lines[i][j]):
                continue
        if i + 1 < 100:
            if int(lines[i + 1][j]) <= int(lines[i][j]):
                continue
        lowPoints.append([i, j])


def isValid(vis, x, y):
    if x < 0 or y < 0 or x >= 100 or y >= 100:
        return False
    if vis[x][y]:
        return False
    return True


# BFS Traversal - assumes grid lines is a global variable
def BFS(vis, row, col):
    q = queue()

    q.append((row, col))
    vis[row][col] = True

    sum = 0
    while len(q) > 0:
        cell = q.popleft()
        y = cell[0]
        x = cell[1]

        sum += 1

        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if isValid(vis, adjy, adjx) and int(lines[adjy][adjx]) != 9:
                q.append((adjy, adjx))
                vis[adjy][adjx] = True

    return sum


vis = [[False for i in range(100)] for i in range(100)]

dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]

basins = [BFS(vis, point[0], point[1]) for point in lowPoints]

result = sorted(basins, reverse=True)[0:3]
print(reduce((lambda x, y: x * y), result))

