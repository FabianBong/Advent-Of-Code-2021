def is_in_area(x, y):
    if 155 >= x >= 135 and -78 >= y >= -102:
        return True
    return False


def one_run(velx, vely):
    x = 0
    y = 0
    while not is_in_area(x, y):
        if x > 155 or y < -102:
            break
        x += velx
        y += vely

        if velx > 0:
            velx -= 1
        elif velx < 0:
            velx += 1

        vely -= 1

    if not is_in_area(x,y):
        return -1
    return 1


# with open("/Users/fabianbong/Documents/Advent_Of_Code/Day_16/input.txt") as f:
#     lines = list(map(lambda x: x.strip(), f.readlines()))

maxYs = []
for i in range(-300,300):
    for j in range(-300,300):
        maxYs.append(one_run(i, j))
        print(i)

print(maxYs.count(1))
