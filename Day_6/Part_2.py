from collections import defaultdict

i = 256;

with open("/Users/fabianbong/Documents/Advent_Of_Code/Day_6/input.txt") as infile:
        vals = infile.read().strip().split(",")

counts = defaultdict(lambda: 0)

for val in (int(v) for v in vals):
        counts[val] += 1

def next_day(c):
    nc = defaultdict(lambda: 0)
    splits = c[0]
    nc[8] = splits
    nc[6] = splits
    for i in range(1, 9):
        nc[i - 1] += c[i]
    return nc

for _ in range(0, i):
    counts = next_day(counts)


print(sum(counts.values()));
