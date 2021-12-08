with open("/Users/fabianbong/Documents/Advent_Of_Code/Day_8/input.txt") as f:
    lines = f.readlines()


def find(patterns, condition):
    for patt in patterns:
        if(condition(patt) == True):
            return patt


def solve(input):
    total = 0
    for line in input.strip().split('\n'):
        patterns, output = line.split(' | ')
        patterns = [set(pattern) for pattern in patterns.split(' ')]
        output = [set(pattern) for pattern in output.split(' ')]

        digit_solution = [''] * 10

        ## We know what 1,4,7 and 8 is based on the digits
        digit_solution[1] = find(patterns, lambda digit: len(digit) == 2)
        digit_solution[7] = find(patterns, lambda digit: len(digit) == 3)
        digit_solution[8] = find(patterns, lambda digit: len(digit) == 7)
        digit_solution[4] = find(patterns, lambda digit: len(digit) == 4)

        ## We can figuer out 0,9 and 6 based on intersects of the sets
        maybe_069 = [digit for digit in patterns if len(digit) == 6]
        digit_solution[6] = find(maybe_069, lambda digit: len(digit & digit_solution[1]) == 1)
        digit_solution[9] = find(maybe_069, lambda digit: len(digit & digit_solution[4]) == 4)
        digit_solution[0] = find(maybe_069, lambda digit: digit != digit_solution[9] and digit != digit_solution[6])

        ## Same idea can be used for 2,3 and 5
        maybe_235 = [digit for digit in patterns if len(digit) == 5]
        digit_solution[3] = find(maybe_235, lambda digit: len(digit & digit_solution[1]) == 2)
        digit_solution[5] = find(maybe_235, lambda digit: len(digit & digit_solution[6]) == 5)
        digit_solution[2] = find(maybe_235, lambda digit: digit != digit_solution[3] and digit != digit_solution[5])

        total_list = [digit_solution.index(out) for out in output]
        total += reduce(lambda acc, digit: 10 * acc + digit, total_list, 0)

    return total

summation = 0;
summation = sum(map(solve, lines))

print(summation)
