def parse_num(numString):
    count = 0
    depth = 0
    depthList = []
    while count < len(numString):
        cur = numString[count]
        if cur == '[':
            depth += 1
        elif cur == ']':
            depth -= 1
        elif cur != ',':
            depthList.append([int(cur), depth])
        count += 1

    return depthList


def add_num(num1, num2):
    sum_num = [[num[0], num[1] + 1] for num in num1 + num2]
    updating = True
    while updating:
        updating = False
        for i in range(len(sum_num)):
            depth = sum_num[i][1]
            if depth >= 5 and depth == sum_num[i + 1][1]:
                if i > 0:
                    sum_num[i - 1][0] += sum_num[i][0]
                if i < len(sum_num) - 2:
                    sum_num[i + 2][0] += sum_num[i + 1][0]
                del sum_num[i:i + 2]
                sum_num.insert(i, [0, depth-1])
                updating = True
                break
        if not updating:
            for i in range(len(sum_num)):
                if sum_num[i][0] > 9:
                    [num, depth] = sum_num[i]
                    rounded_down = num // 2
                    rounded_up = num - num // 2
                    del sum_num[i]
                    sum_num.insert(i, [rounded_up, depth + 1])
                    sum_num.insert(i, [rounded_down, depth + 1])
                    updating = True
                    break
    return sum_num


def calc_magnitude(num):
    while len(num) > 1:
        for i in range(len(num)):
            if i < len(num) - 1 and num[i][1] == num[i+1][1]:
                depth = num[i][1]
                val = 3*num[i][0] + 2*num[i+1][0]
                del num[i:i+2]
                num.insert(i, [val, depth-1])
                break
    return num[0][0]


with open("/Users/fabianbong/Documents/Advent_Of_Code/Day_18/input.txt") as f:
     lines = list(map(lambda x: x.strip(), f.readlines()))

numbers = []
for line in lines:
    numbers.append(parse_num(line))

max_add = -1
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        poss_1 = calc_magnitude(add_num(numbers[i],numbers[j]))
        poss_2 = calc_magnitude(add_num(numbers[j],numbers[i]))
        max_add = max(max_add, poss_1, poss_2)

print(max_add)
