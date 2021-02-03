#(N,M)으로 가는 횟수
from collections import deque
from sys import stdin
import sys
n,m = map(int,stdin.readline().split())
queue = deque()
matrix = []
for _ in range(n):
	lines = stdin.readline().rstrip()
	line = []
	for l in lines:
		line.append(int(l))
	matrix.append(line)

visit = [[0 for _ in range(m)] for _ in range(n)]
#시작점 1,1
def bfs(matrix,visit,queue):
	global cnt
	while queue:
		x,y = queue.popleft()
		#4방향 탐색
		dx = [1,-1,0,0]
		dy = [0,0,1,-1]
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx >=0 and ny >=0 and nx < n and ny < m:
				if matrix[nx][ny] == 1 and visit[nx][ny] == 0:
					visit[nx][ny] = visit[x][y] + 1
					queue.append([nx,ny])

visit[0][0] = 1
queue.append([0,0])
bfs(matrix,visit,queue)

print(visit[n-1][m-1])