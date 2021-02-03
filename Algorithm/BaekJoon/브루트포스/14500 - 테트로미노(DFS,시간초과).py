from sys import stdin
import sys
sys.setrecursionlimit(10**7)
#T Mino를 수정하면 될듯
n,m = map(int,stdin.readline().split())

board = [list(map(int,stdin.readline().split())) for _ in range(n)]


def Tmino(i,j):
	tmino = [[(i,j),(i+1,j),(i,j+1),(i,j-1)],
			 [(i,j),(i-1,j),(i,j+1),(i,j-1)],
			 [(i,j),(i+1,j),(i-1,j),(i,j+1)],
			 [(i,j),(i+1,j),(i-1,j),(i,j-1)]]
	result = 0
	for line in tmino:
		calc = 0
		flag = True 
		for y,x in line:
			if 0<=y<n and 0<=x<m:
				calc += board[y][x]
			else:
				flag = False
				break
		if flag:
			result = max(result,calc)
	return result

maxNum = 0
visit = [[0]*m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(y,x,visit,lens,count):
	global maxNum
	if lens == 4:
		maxNum = max(maxNum,count)
		return
	for i in range(4):
		ny = y+dy[i]
		nx = x+dx[i]

		if 0<=ny<n and 0<=nx<m and visit[ny][nx] == 0:
			visit[ny][nx] = 1
			dfs(ny,nx,visit,lens+1,count+board[ny][nx])
			visit[ny][nx] = 0

for i in range(n):
	for j in range(m):
		visit[i][j] = 1
		dfs(i,j,visit,1,board[i][j])
		visit[i][j] = 0
		maxNum = max(maxNum,Tmino(i,j))
print(maxNum)