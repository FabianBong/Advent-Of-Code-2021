with open("/Users/fabianbong/Documents/Advent_Of_Code/Day_9/input.txt") as f:
    lines = f.readlines()

total = 0
for i in range(0, 100):
    for j in range(0, 100):
        if (j - 1 >= 0):
            if int(lines[i][j - 1]) <= int(lines[i][j]):
                continue
        if (j + 1 < 100):
            if int(lines[i][j + 1]) <= int(lines[i][j]):
                continue
        if (i - 1 >= 0):
            if int(lines[i - 1][j]) <= int(lines[i][j]):
                continue
        if (i + 1 < 100):
            if int(lines[i + 1][j]) <= int(lines[i][j]):
                continue
        total += int(lines[i][j]) + 1
        print(lines[i][j])

print(total)

