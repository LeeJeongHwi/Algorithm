from collections import deque
from sys import stdin
"""
비어 있는 곳   : .
물이 차있는 곳 : *
돌			  : X
비버의 굴 	  : D
고슴도치 위치  : S

매 분마다 고슴도치는 이동
매 분마다 물과 인접해있는 비어있는 칸에 물이 찬다
"""
n,m = map(int,stdin.readline().split())

board = [[x for x in stdin.readline().rstrip()] for _ in range(n)]
hedge = deque()
water = deque()
visit_hedge = [[0]*m for _ in range(n)]
visit_water = [[0]*m for _ in range(n)]
for i in range(n):
	for j in range(m):
		if board[i][j] == 'S':
			hedge.append([i,j])
			visit_hedge[i][j] = 1
		elif board[i][j] == '*':
			water.append([i,j])
			visit_water[i][j] = 1
def bfs():
	while hedge:
		wlen = len(water)
		for i in range(wlen):
			wy,wx = water.popleft()
			for j in range(4):
				wny = wy+dy[j]
				wnx = wx+dx[j]
				if 0<=wny<n and 0<=wnx<m:
					if visit_water[wny][wnx] == 0 and board[wny][wnx] =='.':
						visit_water[wny][wnx] = 1
						water.append([wny,wnx])
		for l in range(len(hedge)):
			y,x = hedge.popleft()
			for i in range(4):
				ny = y+dy[i]
				nx = x+dx[i]
				if 0<=ny<n and 0<=nx<m:
					if visit_hedge[ny][nx] == 0:
						if board[ny][nx] == '.' and visit_water[ny][nx] == 0:
							visit_hedge[ny][nx] = visit_hedge[y][x]+1
							hedge.append([ny,nx])
						elif board[ny][nx] == 'D':
							visit_hedge[ny][nx] = visit_hedge[y][x]+1
							return visit_hedge[ny][nx]-1
	return 'KAKTUS'

dx=[1,-1,0,0]
dy=[0,0,1,-1]

print(bfs())