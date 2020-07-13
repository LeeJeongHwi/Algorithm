from sys import stdin
from collections import deque
n,m = map(int,stdin.readline().split())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]

def target_Search(sy,sx):
	q = deque()
	q.append([sy,sx])
	candidate = deque()
	while q:
		y,x = q.popleft()
		for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
			ny = dy + y
			nx = dx + x
			if 0 <= ny < n and 0 <= nx < m and visit[ny][nx] == 0:
				if maps[ny][nx] == 0:
					visit[ny][nx] = 1
					q.append([ny,nx])
				elif maps[ny][nx] == 1:
					visit[ny][nx] = 2
					candidate.append([ny,nx])
	count = 0
	for i in range(n):
		for j in range(m):	
			if maps[i][j] == 1:
				count +=1
	#melting
	for y,x in candidate:
		maps[y][x] = 0
		visit[y][x] = 1
	if count == 0:
		return False
	global ans
	ans = count
	return True
	
time = 0
ans = 0
while True:
	visit = [[0 for _ in range(m)] for _ in range(n)]
	if not target_Search(0,0):
		break
	time +=1
print(time)
print(ans)