from sys import stdin
from collections import deque

testCase = int(stdin.readline())

def bfs(i,j,farm,visit):
	queue = deque()
	queue.append((i,j))
	dx = [1,-1,0,0]
	dy = [0,0,1,-1]
	while queue:
		y,x = queue.popleft()
		for i in range(4):
			nx = x+dx[i]
			ny = y+dy[i]
			if (0 <= nx < m and 0 <= ny < n):
				if farm[ny][nx] == 1 and visit[ny][nx] == 0:
					visit[ny][nx] = 1
					queue.append((ny,nx))


def solve(m,n,k):
	farm =[[0]*m for _ in range(n)]
	visit =[[0]*m for _ in range(n)]
	for i in range(k):
		x,y = map(int,stdin.readline().split())
		farm[y][x] = 1
	count = 0
	for i in range(n):
		for j in range(m):
			#j == x , i == y
			if farm[i][j] == 1 and visit[i][j] == 0:
				bfs(i,j,farm,visit)
				count+=1
	return count

for _ in range(testCase):
	#가로 m 세로 n 배추갯수 k
	m,n,k = map(int,stdin.readline().split())
	print(solve(m,n,k))