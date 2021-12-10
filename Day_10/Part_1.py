scores1 = {")" : 3, "]" : 57, "}" : 1197, ">" : 25137}
closing = {"(" : ")", "[" : "]", "{": "}", "<" : ">"}

with open("/Users/fabianbong/Documents/Advent_Of_Code/Day_10/input.txt") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

errorScore = 0
for line in lines:
    stack = []
    for charac in line:
        if charac in scores1.keys():
            nextC = stack.pop()
            if charac != closing[nextC]:
                errorScore += scores1[charac]
                break
        else:
            stack.append(charac)


print(errorScore)

