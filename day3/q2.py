
with open("input.txt") as f:
    lines = f.readlines()

count = 0
first, second, third = 0, 1, 2
while third <= len(lines):
    ruck1, ruck2, ruck3 = lines[first].strip(
    ), lines[second].strip(), lines[third].strip()
    common = set(ruck1).intersection(set(ruck2)).intersection(set(ruck3))

    for ch in common:
        if ch.islower():
            count += ord(ch) - 96
        else:
            count += ord(ch) - 38

    first += 3
    second += 3
    third += 3

print(count)
