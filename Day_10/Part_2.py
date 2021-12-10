scores1 = {")" : 3, "]" : 57, "}" : 1197, ">" : 25137}
scores2 =  {")" : 1, "]" : 2, "}" : 3, ">" : 4}
closing = {"(" : ")", "[" : "]", "{": "}", "<" : ">"}

with open("/Users/fabianbong/Documents/Advent_Of_Code/Day_10/input.txt") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

completionScore = []
for line in lines:
    stack = []
    error = 0
    for charac in line:
        if charac in scores1.keys():
            nextC = stack.pop()
            if charac != closing[nextC]:
                error = 1
                break
        else:
            stack.append(charac)
    if error == 0:
        score = 0
        while len(stack) != 0:
            score = score * 5 + scores2[closing[stack.pop()]]
        completionScore.append(score)


print(sorted(completionScore)[len(completionScore) // 2])


