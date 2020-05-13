#solution : https://www.acmicpc.net/board/view/24596
from sys import stdin,setrecursionlimit
setrecursionlimit(10**8)
n,m = map(int,stdin.readline().split())

maze = [list(map(int,stdin.readline().split())) for _ in range(n)]
memo = [[-1]*m for _ in range(n)]

def dp(y,x):
	if y<0 or x<0:
		return 0
	
	if memo[y][x] == -1:
		memo[y][x] = maze[y][x]+ max(dp(y-1,x),dp(y,x-1)) # y-1,x-1은 없어도 됨(비효율적이므로)
	
	return memo[y][x]

memo[0][0] = maze[0][0]
dp(n-1,m-1)

print(memo[n-1][m-1])

#더 나은 풀이 : https://pacific-ocean.tistory.com/204
from sys import stdin
n,m = map(int,stdin.readline().split())
dp = [[0]*(m+1) for _ in range(n+1)]
maze = [list(map(int,stdin.readline().split())) for _ in range(n)]

for i in range(1,n+1):
	for j in range(1,m+1):
		dp[i][j] = maze[i-1][j-1]+max(dp[i-1][j],dp[i][j-1])
print(dp[n][m])