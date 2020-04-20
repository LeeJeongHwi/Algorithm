from sys import stdin
import copy
import sys
sys.setrecursionlimit(10**8)
#적록색약은 빨간색과 초록색의 차이를 거의 못 느낀다.
#나중에 BFS 로 풀어보자
n = int(stdin.readline())

maps = [[x for x in stdin.readline().rstrip()] for _ in range(n)]

ans = [0,0]

def check(maps):
	for i in range(n):
		for j in range(n):
			if maps[i][j]=='G':
				maps[i][j]='R'

def dfs(y,x,color,maps,visit):
	visit[y][x] = 1
	for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
		ny = y+dy
		nx = x+dx
		if 0<=ny<n and 0<=nx<n and visit[ny][nx] == 0 and maps[ny][nx]==color:
			dfs(ny,nx,color,maps,visit)

visit_n = [[0]*n for _ in range(n)]
visit_rg = [[0]*n for _ in range(n)]

maps_rg = copy.deepcopy(maps)
check(maps_rg)



for i in range(n):
	for j in range(n):
		if visit_n[i][j] == 0:
			ans[0] += 1
			dfs(i,j,maps[i][j],maps,visit_n)
		if visit_rg[i][j] == 0:
			ans[1] += 1
			dfs(i,j,maps_rg[i][j],maps_rg,visit_rg)
print(*ans)