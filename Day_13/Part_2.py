import matplotlib.pyplot as plt


def fold_y(points_passed, y):
    new_points = []
    for point in points_passed:
        if point[1] > y:
            new_y = y - (point[1] - y)
            if new_y >= 0 and [point[0],new_y] not in new_points:
                new_points.append([point[0], new_y])
        else:
            if [point[0],point[1]] not in new_points:
                new_points.append([point[0], point[1]])
    return new_points


def fold_x(points_passed, x):
    new_points = []
    for point in points_passed:
        if point[0] > x:
            new_x = x - (point[0] - x)
            if new_x >= 0 and [new_x, point[1]] not in new_points:
                new_points.append([new_x, point[1]])
        else:
            if [point[0],point[1]] not in new_points:
                new_points.append([point[0], point[1]])
    return new_points


with open("/Users/fabianbong/Documents/Advent_Of_Code/Day_13/input.txt") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

points = []

# Go through all given points
for i in range(866):
    line = lines[i].strip().split(',')
    points.append([int(line[0]), int(line[1])])

# Fold the paper
for i in range(867, 879):
    line = lines[i].strip().split(' ')
    fold = line[2].strip().split('=')
    if fold[0] == "x":
        points = fold_x(points, int(fold[1]))
    else:
        points = fold_y(points, int(fold[1]))
    print(len(points))

x = [point[0] for point in points]
y = [-point[1] for point in points]  # To flip the plot

plt.scatter(x=x, y=y)
plt.savefig('books_read.png')

