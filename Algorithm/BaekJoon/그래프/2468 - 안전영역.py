from sys import stdin
from collections import deque
import copy
#DFS 로 풀면 시간단축이 가능하다.
n = int(stdin.readline())

domain = []
for i in range(n):
	line = list(map(int,stdin.readline().split()))
	domain.append(line)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(maps,height,q,visited):
	while q:
		y,x = q.popleft()
		for i in range(4):
			ny = y+dy[i]
			nx = x+dx[i]
			if 0<=ny<n and 0<=nx<n:
				if maps[ny][nx]>height and visited[ny][nx]==0:
					visited[ny][nx] = 1
					q.append((ny,nx))

maxCount = 0
visit = [[0]*n for _ in range(n)]
for height in range(101):
	visited = copy.deepcopy(visit)
	q=deque()
	count = 0
	for i in range(n):
		for j in range(n):
			if domain[i][j]>height and visited[i][j] == 0:
				count+=1
				q.append((i,j))
				visited[i][j] = 1
				bfs(domain,height,q,visited)
	# for i in visited:
	# 	print(i)
	# print(count)
	if count == 0:
		break
	maxCount= max(maxCount,count)
	# print("=========")
print(maxCount)