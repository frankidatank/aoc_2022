score_sign = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

res_sign = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

match_points = {
    'lose': 0,
    'win': 6,
    'draw': 3
}

signs_p1 = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

sings_p1_to_int = {
    'A': 1,
    'B': 2,
    'C': 3,
}


def what_shape(needed_outcome, p1_shape):
    p1 = signs_p1[p1_shape]
    if needed_outcome == 'draw':
        return sings_p1_to_int[p1_shape]
    if needed_outcome == 'win':
        if p1 == 'paper':
            return 3
        if p1 == 'scissors':
            return 1
        return 2
    if needed_outcome == 'lose':
        if p1 == 'paper':
            return 1
        if p1 == 'scissors':
            return 2
        return 3


with open('input.txt') as f:
    lines = f.readlines()

score = 0

for turn in lines:
    turn_stripped = turn.strip()
    p1, p2 = turn_stripped[0], turn_stripped[2]
    score += what_shape(res_sign[p2], p1) + match_points[res_sign[p2]]

print(score)
