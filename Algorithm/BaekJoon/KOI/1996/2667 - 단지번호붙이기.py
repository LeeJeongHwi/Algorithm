from sys import stdin
from collections import deque

n = int(input())
maps = [[int(x) for x in stdin.readline().rstrip()] for _ in range(n)]
visit = [[0 for _ in range(n)] for _ in range(n)]

numbers = []
def bfs(sy,sx,number):
	queue = deque()
	queue.append((sy,sx))
	visit[sy][sx] = number
	count = 1
	while queue:
		y,x = queue.popleft()
		for dy,dx in [(1,0),(-1,0),(0,-1),(0,1)]:
			ny = dy+y
			nx = dx+x
			if 0<=ny<n and 0<=nx<n:
				if maps[ny][nx] and not visit[ny][nx]:
					queue.append((ny,nx))
					visit[ny][nx] = number
					count+=1
	if count:
		numbers.append(count)
number = 0
for i in range(n):
	for j in range(n):
		if visit[i][j] == 0 and maps[i][j]==1:
			number+=1
			bfs(i,j,number)
numbers.sort()
print(number)
print(*numbers, sep='\n')
