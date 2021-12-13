## Solution still in work!

with open("/Users/fabianbong/Documents/Advent_Of_Code/Day_12/input.txt") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

graph = {}
for line in lines:
    a, b = line.split('-')
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)


## This part is still in work - but works.
def dfs(cave, visited, one_off):
    if cave == "end": return 1
    if cave.islower(): visited.add(cave)
    total = sum([dfs(i, visited, one_off) for i in graph[cave] if not i in visited])
    total += 0 if one_off != ' ' else sum([dfs(i, visited, i) for i in graph[cave] if i in visited and i != 'start'])
    if (cave != one_off): visited.discard(cave)
    return total;

print ('Part 1:', dfs("start", set(), ''))
