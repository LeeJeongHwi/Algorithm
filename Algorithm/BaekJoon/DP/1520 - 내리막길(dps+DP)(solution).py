#solution : https://chldkato.tistory.com/114
from sys import stdin,setrecursionlimit
setrecursionlimit(10**8)

n,m = map(int,stdin.readline().split())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]

memo = [[-1 for _ in range(m)] for _ in range(n)]

def dfs(y,x):
	if (y,x) == (n-1,m-1):
		return 1
	if memo[y][x] != -1:
		return memo[y][x]

	memo[y][x] = 0
	if y+1<n and maps[y][x] > maps[y+1][x]:
		memo[y][x]+=dfs(y+1,x)
	if 0<=y-1 and maps[y][x] > maps[y-1][x]:
		memo[y][x]+=dfs(y-1,x)
	if x+1<m and maps[y][x] > maps[y][x+1]:
		memo[y][x]+=dfs(y,x+1)
	if 0<=x-1 and maps[y][x] > maps[y][x-1]:
		memo[y][x]+=dfs(y,x-1)
	return memo[y][x]
print(dfs(0,0))