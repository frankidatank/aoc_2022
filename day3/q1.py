
with open("input.txt") as f:
    lines = f.readlines()

count = 0

for ruck in lines:
    ruck = ruck.strip()
    left, right = ruck[:len(ruck) // 2], ruck[len(ruck) // 2:]

    # find ch's that appear in both left and right
    both = set(left).intersection(set(right))

    for ch in both:
        if ch.islower():
            count += ord(ch) - 96
        else:
            count += ord(ch) - 38

print(count)
