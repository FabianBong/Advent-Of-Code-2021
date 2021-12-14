with open("/Users/fabianbong/Documents/Advent_Of_Code/Day_14/input.txt") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

polymer = lines[0]

patterns = dict()
for i in range(2, 102):
    line = lines[i].rstrip('\n').split('->')
    patterns[line[0].strip(' ')] = line[1].strip(' ')

pairs = {patt: polymer.count(patt) for patt in patterns}
chars = {char: polymer.count(char) for char in patterns.values()}

for i in range(40):
    for pair, count in pairs.copy().items():
        pairs[pair] -= count
        pairs[pair[0] + patterns[pair]] += count
        pairs[patterns[pair] + pair[1]] += count
        chars[patterns[pair]] += count

print(max(chars.values()) - min(chars.values()))


