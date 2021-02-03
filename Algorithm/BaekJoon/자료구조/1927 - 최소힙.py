from sys import stdin
import heapq

n = int(stdin.readline())
heap =[]
for _ in range(n):
	x = int(stdin.readline())
	if x == 0:
		if not heap:
			print(0)
		else:
			print(heapq.heappop(heap))
	else:
		heapq.heappush(heap,x)