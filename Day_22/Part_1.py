import collections

def valid_cube(x,y,z):
    if -50 <= x <= 50 and -50 <= y <= 50 and -50 <= z <= 50:
        return True
    return False

with open("/Users/fabianbong/Documents/Advent_Of_Code/Day_22/input.txt") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

cubes = collections.Counter()

for line in lines:
    turning = line.split(" ")
    sign = 1 if turning[0] == 'on' else -1
    coord = turning[1].split(',')
    x = coord[0].strip('x=').split('..')
    y = coord[1].strip('y=').split('..')
    z = coord[2].strip('z=').split('..')
    update = collections.Counter()

    if not valid_cube(int(x[0]), int(y[0]), int(z[0])):
        continue

    for (ex_x0,ex_x1, ex_y0, ex_y1, ex_z0, ex_z1), ex_sign in cubes.items():
        intersect_x0 = max(int(x[0]), ex_x0)
        intersect_x1 = min(int(x[1]), ex_x1)
        intersect_y0 = max(int(y[0]), ex_y0)
        intersect_y1 = min(int(y[1]), ex_y1)
        intersect_z0 = max(int(z[0]), ex_z0)
        intersect_z1 = min(int(z[1]), ex_z1)

        if intersect_x0 <= intersect_x1 and intersect_y0 <= intersect_y1 and intersect_z0 <= intersect_z1:
            update[(intersect_x0,intersect_x1, intersect_y0, intersect_y1, intersect_z0, intersect_z1)] -= ex_sign

    if sign > 0:
        update[(int(x[0]), int(x[1]), int(y[0]), int(y[1]), int(z[0]), int(z[1]))] += sign

    cubes.update(update)

print(sum((x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1) * sgn
          for (x0, x1, y0, y1, z0, z1), sgn in cubes.items()))

