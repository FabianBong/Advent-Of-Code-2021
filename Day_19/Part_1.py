import itertools
from collections import Counter

with open("/Users/fabianbong/Documents/Advent_Of_Code/Day_19/input.txt") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

scanners = []
cur = []
for line in lines:
    if "---" in line:
        cur = []
        scanners.append(cur)
        continue
    if line == "":
        continue
    cur.append(tuple(map(int, line.split(","))))


def try_align(aligned, candidate):
    ret = []
    dl = []
    dp = dpp = None
    for dim in range(3):
        x = [pos[dim] for pos in aligned]
        for (d, s) in [(0, 1), (1, 1), (2, 1), (0, -1), (1, -1), (2, -1)]:
            if d == dp or d == dpp:
                continue
            t = [pos[d] * s for pos in candidate]
            w = [b - a for (a, b) in itertools.product(x, t)]
            c = Counter(w).most_common(1)
            if c[0][1] >= 12:
                break
        if c[0][1] < 12:
            return None
        (dpp, dp) = (dp, d)
        ret.append([v - c[0][0] for v in t])
        dl.append(c[0][0])
    return list(zip(ret[0], ret[1], ret[2])), dl


done = set()
next = [scanners[0]]
rest = scanners[1:]
shifts = []
while next:
    aligned = next.pop()
    tmp = []
    for candidate in rest:
        r = try_align(aligned, candidate)
        if r:
            (updated, shift) = r
            shifts.append(shift)
            next.append(updated)
        else:
            tmp.append(candidate)
    rest = tmp
    done.update(aligned)


## How many scanners
print(len(done))
sxs = itertools.product(shifts, shifts)
