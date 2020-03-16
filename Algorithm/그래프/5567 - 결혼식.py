from sys import stdin
from collections import deque
n = int(stdin.readline())

m = int(stdin.readline())

graph = [[]*(n+1) for _ in range(n+1)]

for _ in range(m):
	p,c = map(int,stdin.readline().split())
	graph[p].append(c)
	graph[c].append(p)
part = set()

for i in graph[1]:
	part.add(i)
	for j in graph[i]:
		if j != 1:
			part.add(j)
print(len(part))