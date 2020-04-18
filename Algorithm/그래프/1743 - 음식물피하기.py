from sys import stdin
import sys
sys.setrecursionlimit(10**8)
n,m,k = map(int,stdin.readline().split())

maps = [[0]*m for _ in range(n)]
visit = [[0]*m for _ in range(n)]

for i in range(k):
	y,x = map(int,stdin.readline().split())
	maps[y-1][x-1] = 1

maxfood = 0
def dfs(y,x):
	global maxfood,size
	size+=1
	visit[y][x] = size
	if size >= maxfood:
		maxfood=size

	for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
		ny = y+dy
		nx = x+dx
		if 0<=ny<n and 0<=nx<m:
			if visit[ny][nx] == 0 and maps[ny][nx] == 1:
				dfs(ny,nx)

for i in range(n):
	for j in range(m):
		if visit[i][j] ==0 and maps[i][j]==1:
			size = 0
			dfs(i,j)

for i in visit:
	print(i)

print(maxfood)
