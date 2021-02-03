import sys
from collections import deque

sys.setrecursionlimit(10**6)

n,m = map(int,sys.stdin.readline().split())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
visit = [False] * (n+1)

def dfs(now):
	visit[now] = True
	for i in range(1,n+1):
		if graph[now][i] == 1 and visit[i] is False:
			dfs(i)


for _ in range(m):
	x,y = map(int,sys.stdin.readline().split())
	graph[x][y] = 1
	graph[y][x] = 1

count = 0


for i in range(1,n+1):
	if not visit[i]:
		dfs(i)
		count+=1

print(count)
