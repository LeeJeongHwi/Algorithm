"""
https://yabmoons.tistory.com/194
"""
from sys import stdin
n,m,k = map(int,stdin.readline().split())
matrix = []

for i in range(n):
	line = [x for x in stdin.readline().rstrip()]
	matrix.append(line)

dic = [x for x in stdin.readline().rstrip()]
diclen = len(dic)

memo = [[[-1 for _ in range(101)] for _ in range(101)] for _ in range(81)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y,idx):
	if memo[idx][x][y] != -1:
		return memo[idx][x][y]
	if idx >= diclen:
		return 1

	memo[idx][x][y] = 0

	for a in range(4):
		for b in range(1,k+1): #k칸수만큼 더 이동가능
			nx = x+dx[a]*b
			ny = y+dy[a]*b
			if (0 <= nx < n) and (0 <= ny < m):
				if matrix[nx][ny] == dic[idx]:
					memo[idx][x][y] += dfs(nx,ny,idx+1)
				else:
					continue
			else:
				continue
	return memo[idx][x][y]

ans = 0
for i in range(n):
	for j in range(m):
		if matrix[i][j] == dic[0]:
			ans += dfs(i,j,1)
print(ans)
