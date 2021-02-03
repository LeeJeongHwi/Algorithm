from sys import stdin
from collections import deque

n,m = map(int,stdin.readline().split())

maps = [list(stdin.readline().rstrip()) for _ in range(n)]
maxHour = 0
def bfs(visit,sy,sx):
	global maxHour
	queue = deque()
	queue.append((sy,sx))
	
	while queue:
		y,x = queue.popleft()
		maxHour = max(visit[y][x] - visit[sy][sx],maxHour)
		for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]: #이방식은 사실 시간이 오래걸림
			ny = y+dy
			nx = x+dx
			if 0<=ny<n and 0<=nx<m and visit[ny][nx] == 0:
				if maps[ny][nx] == 'L':
					visit[ny][nx] += visit[y][x]+1
					queue.append((ny,nx))

for i in range(n):
	for j in range(m):
		if maps[i][j] == 'L':
			visit = [[0]*m for _ in range(n)]
			visit[i][j] = 1
			bfs(visit,i,j)
print(maxHour)