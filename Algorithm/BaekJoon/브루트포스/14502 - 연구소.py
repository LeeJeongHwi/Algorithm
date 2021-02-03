from sys import stdin
from collections import deque
import copy
n,m = map(int,stdin.readline().split())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]

virus = deque()
zero_map = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

#initial
for i in range(n):
	for j in range(m):
		if maps[i][j] == 2:
			virus.append((i,j))
		elif maps[i][j] == 0:
			zero_map.append((i,j))

zero_len = len(zero_map)

def setWall():
	maxCount = 0
	for i in range(0,zero_len-2):
		for j in range(i+1,zero_len-1):
			for k in range(j+1,zero_len):
				y1,x1 = zero_map[i]
				y2,x2 = zero_map[j]
				y3,x3 = zero_map[k]

				newmaps = copy.deepcopy(maps)
				newmaps[y1][x1]=1
				newmaps[y2][x2]=1
				newmaps[y3][x3]=1
				
				maxCount = max(setVirus(newmaps,copy.deepcopy(virus)),maxCount)
	return maxCount
def countZero(maps):
	count = 0
	for i in maps:
		count+=i.count(0)
	return count

def setVirus(maps,viruses):
	while viruses:
		y,x = viruses.pop()
		for i in range(4):
			ny=y+dy[i]
			nx=x+dx[i]
			if 0<=ny<n and 0<=nx<m:
				if maps[ny][nx] == 0:
					maps[ny][nx] = 2
					viruses.append((ny,nx))
	return countZero(maps)

print(setWall())