from sys import stdin
import heapq

n , m = map(int,stdin.readline().split())

matrix = []
for _ in range(m):
	matrix.append(list(stdin.readline().rstrip()))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

visit = [[0] * n for _ in range(m)]

def bfs(start,maps,visited):
	queue = []
	heapq.heappush(queue,start)
	visited[0][0] = 1
	while queue:
		cnt,cx,cy = heapq.heappop(queue)
		if cx == m - 1 and cy == n - 1:
			return cnt
		for i in range(4):
			nx = cx + dx[i]
			ny = cy + dy[i]
			if 0 <= nx < m and 0 <= ny < n:
				if visited[nx][ny] == 1:
					continue
				elif matrix[nx][ny] == '1':
					heapq.heappush(queue,(cnt+1,nx,ny))
				elif matrix[nx][ny] == '0':
					heapq.heappush(queue,(cnt,nx,ny))
				visited[nx][ny] = 1

print(bfs((0,0,0),matrix,visit))