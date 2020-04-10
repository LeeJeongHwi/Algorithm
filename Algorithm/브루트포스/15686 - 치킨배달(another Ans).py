#solution : https://www.acmicpc.net/source/13963691
from sys import stdin
from itertools import combinations
n , m = map(int,stdin.readline().split())
city = [list(map(int,stdin.readline().split())) for _ in range(n)]
ch = []
house = []
for i in range(n):
	for j in range(n):
		if city[i][j] == 2:
			ch.append((i,j))
		elif city[i][j] == 1:
			house.append((i,j))

distance = []
for h in house:
	dis = []
	for c in ch:
		dis.append(abs(c[0]-h[0])+abs(c[1]-h[1]))
	distance.append(dis)
min_v = float('inf')
for sel in combinations(range(len(ch)),m):
	sum_v = 0
	for dis in distance:
		sum_v += min([dis[i] for i in sel])
	min_v = min(sum_v,min_v)
print(min_v)