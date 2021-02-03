from sys import stdin
n=int(stdin.readline())

maze = list(map(int,stdin.readline().split()))

dp = [1000 for _ in range(n)]
dp[0] = 0
for i in range(n):
	for j in range(maze[i],0,-1):
		if j+i <= n-1:
			dp[j+i] = min(dp[j+i],dp[i]+1)
if dp[n-1] == 1000:
	print(-1)
else:
	print(dp[n-1])