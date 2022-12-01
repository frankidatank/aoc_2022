import math
import heapq

total = 0
max_ = -math.inf
heap = []
with open('data.txt') as f:
	lines = f.readlines()
for nums in lines:
	if nums == "\n":
		heapq.heappush(heap, total)
		total = 0
		if len(heap) > 3:
			heapq.heappop(heap)
	else:
		total += int(nums.strip())

res = 0
while heap:
	res += heapq.heappop(heap)
print(res)



	

