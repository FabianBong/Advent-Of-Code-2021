import collections


def insert(string, patterns):
    i = 1
    while i < len(string):
        ins = False
        part = string[i - 1:i + 1]
        for patt in patterns:
            if part == patt[0]:
                string = string[:i] + patt[1] + string[i:]
                ins = True
                break
        if not ins:
            i += 1
        else:
            i += 2
    return string


with open("/Users/fabianbong/Documents/Advent_Of_Code/Day_14/input.txt") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

polymer = lines[0]
patterns = []

for i in range(2, 102):
    line = lines[i].rstrip('\n').split('->')
    pattern = line[0].rstrip(' ')
    ins = line[1][1]
    patterns.append([pattern,ins])

for i in range(10):
    polymer = insert(polymer,patterns)



common = collections.Counter(polymer).most_common()
result = common[0][1] - common[len(common)-1][1]
print(result)

