from sys import stdin
from collections import deque

t = int(stdin.readline())

def spread_Fire(fq,maps):
	#Spread Fire
	for fire in range(len(fq)):
		y,x = fq.popleft()
		for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
			ny = y+dy
			nx = x+dx
			if 0<=ny<m and 0<=nx<n:
				if maps[ny][nx] =='.':
					maps[ny][nx] ='*'
					fq.append((ny,nx))
def move_Human(hq,visit):
	#Move Human
	for fire in range(len(hq)):
		y,x = hq.popleft()
		for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
			ny = y+dy
			nx = x+dx
			if 0<=ny<m and 0<=nx<n:
				if maps[ny][nx] =='.' and visit[ny][nx] ==0:
					visit[ny][nx] = visit[y][x] + 1
					hq.append((ny,nx))
			elif not(0<=ny<m) or not(0<=nx<n):
				print(visit[y][x]+1)
				return True
	return False
def bfs(maps,fq,hq,visit):
	while hq:
		spread_Fire(fq,maps)
		if move_Human(hq,visit):
			return
	print("IMPOSSIBLE")
for _ in range(t):
	n,m = map(int,stdin.readline().split()) #(n이 가로 m이 세로)
	maps = [list(stdin.readline().rstrip()) for _ in range(m)]
	fire_queue = deque()
	human_queue= deque()
	#Find Fire
	for i in range(m):
		for j in range(n):
			if maps[i][j] == '*':
				fire_queue.append((i,j))
			if maps[i][j] == '@':
				human_queue.append((i,j))
	#BFS
	visit = [[0]*n for _ in range(m)]
	bfs(maps,fire_queue,human_queue,visit)
