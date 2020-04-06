from sys import stdin
from collections import deque
n,m = map(int,stdin.readline().split())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]

q = deque()
for i in range(n):
	for j in range(m):
		if maps[i][j] == 2:
			q.append((i,j))

dx=[1,-1,0,0]
dy=[0,0,1,-1]


def bfs():

