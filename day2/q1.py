score_sign = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

signs_p2 = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

signs_p1 = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}


def p2_score(p1, p2):
    p1, p2 = signs_p1[p1], signs_p2[p2]
    if p2 == 'rock' and p1 == 'scissors':
        return 6
    if p2 == 'scissors' and p1 == 'paper':
        return 6
    if p2 == 'paper' and p1 == 'rock':
        return 6
    if p2 == 'rock' and p1 == 'rock':
        return 3
    if p2 == 'paper' and p1 == 'paper':
        return 3
    if p2 == 'scissors' and p1 == 'scissors':
        return 3
    return 0

    return False


with open('input.txt') as f:
    lines = f.readlines()

score = 0

for turn in lines:
    turn_stripped = turn.strip()
    p1, p2 = turn_stripped[0], turn_stripped[2]
    score += p2_score(p1, p2) + score_sign[p2]

print(score)
