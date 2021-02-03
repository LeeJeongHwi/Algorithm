"""

"""
from collections import deque
from sys import stdin

n = int(stdin.readline())
matrix = [list(map(int,stdin.readline().split())) for _ in range (n)]
visit = [[0]*n for _ in range(n)]
island = 0
min_ = 1e9
dx,dy= [1,-1,0,0],[0,0,1,-1]
#섬 번호 지정
def bfs_island(matrix,visit,island,x,y):
	queue = deque()
	queue.append([x,y])
	while queue:
		x,y = queue.popleft()
		visit[x][y] = 1
		#4방향 탐색
		matrix[x][y] = island
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx >= 0 and nx < n and ny >= 0 and ny < n:
				if matrix[nx][ny] != 0 and visit[nx][ny] == 0 :
					queue.append([nx,ny])
					visit[nx][ny] = 1
"""
BFS는 큐에서 꺼낼 때 방문표시를 하는 게 아니라,
큐에 넣을 때 해야 중복 방문이 일어나지 않는다. ** 중요 **
"""
for i in range(n):
	for j in range(n):
		if matrix[i][j] == 1 and visit[i][j] == 0:
			island += 1
			bfs_island(matrix,visit,island,i,j)

def getDistance(island):
	global min_
	distance = [[-1]*n for _ in range(n)]
	q = deque()
	for y in range(n):
		for x in range(n):
			if matrix[y][x] == island:
				q.append([x,y])
				distance[y][x] = 0
	while q:
		x,y= q.popleft()
		for i in range(4):
			nx,ny = x+dx[i],y+dy[i]
			if nx >= 0 and nx < n and ny >= 0 and ny <n:
				if matrix[ny][nx] != island and matrix[ny][nx] != 0 :
					min_ = min(min_,distance[y][x])
					return
				if distance[ny][nx] == -1 and matrix[ny][nx] == 0 :
					distance[ny][nx] = distance[y][x] + 1
					q.append([nx,ny])
for i in range(1,island):
	getDistance(i)
print(min_)