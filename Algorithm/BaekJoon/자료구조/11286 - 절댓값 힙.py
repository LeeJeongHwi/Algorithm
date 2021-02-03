"""
# PriorityQueue 방식

from sys import stdin
from queue import PriorityQueue

n = int(stdin.readline())

pq = PriorityQueue()
for _ in range(n):
	x = int(stdin.readline())
	if x==0:
		if not pq.empty():
			print(pq.get()[1])
		else:
			print(0)
	else:
		pq.put((abs(x),x))
"""
#HeapQ 방식
from sys import stdin
import heapq

n = int(stdin.readline())
heap = []
for _ in range(n):
	x = int(stdin.readline())
	if x == 0:
		if heap:
			print(heapq.heappop(heap)[1])
		else:
			print(0)
	else:
		heapq.heappush(heap,(abs(x),x))