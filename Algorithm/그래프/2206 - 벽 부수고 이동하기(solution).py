#solution : https://hello70825.tistory.com/82
from sys import stdin
from collections import deque

n,m = map(int,stdin.readline().split())


graph = []
for i in range(n):
	graph.append([int(x) for x in stdin.readline().rstrip()])

visit = [[[0]*2 for _ in range(m)] for _ in range(n)]

def bfs(a,b,c,visit):
	queue = deque()
	queue.append((a,b,c))
	visit[a][b][c] = 1
	while queue:
		x,y,z=queue.popleft()
		if x == m-1 and y==n-1:
			break
		for i in [(1,0),(-1,0),(0,1),(0,-1)]:
			nx = x+i[1]
			ny = y+i[0]
			if 0<=nx<m and 0<=ny<n:
				if visit[ny][nx][z] == 0 and graph[ny][nx]== 0:
					visit[ny][nx][z] += visit[y][x][z]+1
					queue.append((nx,ny,z))
				if visit[ny][nx][z] == 0 and graph[ny][nx] == 1 and z==0:
					visit[ny][nx][z+1] = visit[y][x][z]+1
					queue.append((nx,ny,z+1))
	if visit[n-1][m-1][0] != 0:
		if visit[n-1][m-1][1] != 0:
			return min(visit[n-1][m-1][0],visit[n-1][m-1][1])
		else:
			return visit[n-1][m-1][0]
	elif visit[n-1][m-1][1] == 0:
		return -1
	else:
		return visit[n-1][m-1][1]

print(bfs(0,0,0,visit))
