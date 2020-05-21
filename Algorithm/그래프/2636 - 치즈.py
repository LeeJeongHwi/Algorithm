from sys import stdin
from collections import deque
n,m = map(int,stdin.readline().split())
cheeze = [list(map(int,stdin.readline().split())) for _ in range(n)]

def bfs(visit,i,j):
	global cheeze,rest_Cheeze
	queue = deque()
	queue.append((i,j))
	visit[i][j] = -1
	c = []
	while queue:
		y,x = queue.popleft()
		#0 부분 탐색
		for dy,dx in [(0,1),(1,0),(-1,0),(0,-1)]:
			ny = y+dy
			nx = x+dx
			if 0<=ny<n and 0<=nx<m and visit[ny][nx] == 0:
				if cheeze[ny][nx] == 0:
					visit[ny][nx] = -1
					queue.append((ny,nx))
				elif cheeze[ny][nx] == 1:
					visit[ny][nx] = 1
					c.append((ny,nx))
	for y,x in c:
		cheeze[y][x] = 0
	rest_Cheeze = len(c)

rest_Cheeze = 0
def search_Cheeze():
	count = 0
	while True:
		visit = [[0 for _ in range(m)] for _ in range(n)]
		bfs(visit,0,0)
		cheeze_Count = 0
		for i in range(n):
			for j in range(m):
				if cheeze[i][j] == 1:
					cheeze_Count+=1
		if cheeze_Count == 0:
			return count
		count+=1
t = search_Cheeze()
print(t+1)
print(rest_Cheeze)