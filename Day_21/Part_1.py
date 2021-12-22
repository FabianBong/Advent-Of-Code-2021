score = [1,2,3,4,5,6,7,8,9,10]

## Player 1 starting position
p1 = 10 -1
p1score = 0

## Player 2 starting position
p2 = 9 -1
p2score = 0

curDie = 1
curPlayer = True
die_rolls = 0
while p1score < 1000 and p2score < 1000:
    roll = curDie + curDie + 1 + curDie + 2
    curDie +=3
    die_rolls += 3
    if curPlayer:
        p1 = (p1+roll) % 10
        p1score += score[p1]
        curPlayer = False
    else:
        p2 = (p2 + roll) % 10
        p2score += score[p2]
        curPlayer = True


print(min(p1score,p2score) * die_rolls)

# 1 2 3 4 5 6 7 8 9 10
# 0 1 2 3 4 5 6 7 8 9
