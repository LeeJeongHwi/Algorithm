from sys import stdin
from collections import deque
row,col,floor = map(int,stdin.readline().split())

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

box = [[0]*col for _ in range(floor)]
for i in range(floor):
	for j in range(col):
		box[i][j]=list(map(int,stdin.readline().split()))
count = -1
def bfs(box):
	global count
	queue = deque()
	for i in range(floor):
		for j in range(col):
			for k in range(row):
				if box[i][j][k] == 1:
					queue.append((k,j,i))
	while queue:
		qlen = len(queue)
		count+=1
		for _ in range(qlen):
			x,y,z = queue.popleft()
			for i in range(6):
				nx,ny,nz = x+dx[i],y+dy[i],z+dz[i]
				if 0<=nx<row and 0<=ny<col and 0<=nz<floor:
					if box[nz][ny][nx] == 0:
						box[nz][ny][nx] = 1
						queue.append((nx,ny,nz))
					
	for i in range(floor):
		for j in range(col):
			for k in range(row):
				if box[i][j][k] == 0:
					count = -1
					return
				else:
					if count == -1:
						count = 0

bfs(box)
print(count)