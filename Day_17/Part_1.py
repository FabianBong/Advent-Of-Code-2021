def is_in_area(x, y):
    if x <= 155 and x >= 135 and y <= -78 and y >= -102:
        return True
    return False


def one_run(velx, vely):
    x = 0
    y = 0
    maxY = 0
    while not is_in_area(x, y):
        if x > 155 or y < -102:
            break
        x += velx
        y += vely
        if y > maxY:
            maxY = y

        if velx > 0:
            velx -= 1
        elif velx < 0:
            velx += 1

        vely -= 1

    if not is_in_area(x,y):
        return -1
    return maxY


# with open("/Users/fabianbong/Documents/Advent_Of_Code/Day_16/input.txt") as f:
#     lines = list(map(lambda x: x.strip(), f.readlines()))

maxYs = []
for i in range(1,700):
    for j in range(1,700):
        maxYs.append(one_run(i, j))
        print(i)

print(max(maxYs))
