import math

total = 0
max_ = -math.inf
with open('data.txt') as f:
    lines = f.readlines()
for nums in lines:
    if nums == "\n":
        max_ = max(max_, total)
        total = 0
    else:
        total += int(nums.strip())

print(max_)
