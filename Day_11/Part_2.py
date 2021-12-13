def getadjcells(arr, i, j):
    possible = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    adj = [(i + poss[0], j + poss[1]) for poss in possible if 0 <= i + poss[0] <= len(arr) - 1 and
           0 <= j + poss[1] <= len(arr[0]) - 1]
    return adj


def flashes(arr, fl):
    for f in fl:
        neighbors = getadjcells(arr, f[0], f[1])
        for x, y in neighbors:
            if arr[x][y] != 0:
                arr[x][y] = (arr[x][y] + 1) % 10
                if arr[x][y] == 0:
                    fl.append((x, y))
            else:
                arr[x][y] = 0
    return (arr)


def incrementby1(arr):
    arr = [[(arr[i][j] + 1) % 10 for i in range(len(arr))] for j in range(len(arr[0]))]
    flashing_octopi = [(i,j) for i in range(len(arr)) for j in range(len(arr[0])) if arr[i][j] == 0]
    return arr, flashing_octopi

with open("/Users/fabianbong/Documents/Advent_Of_Code/Day_11/input.txt") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

s = [[int(item) for item in line] for line in lines]

step = 0;total = 0
while sum(sum(s, [])) != 0:
    s, flashing_octopi = incrementby1(s)
    s = flashes(s, flashing_octopi)
    ze = sum([sum([True for i in row if not i]) for row in s])
    total += ze
    step += 1

print(step)

