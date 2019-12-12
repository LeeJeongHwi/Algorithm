from sys import stdin

n,k=map(int,stdin.readline().split())

dp = [[1 for _ in range(201)] for _ in range(201)] #1로 초기화

# i == n / j == k

for j in range(1,k+1):
	dp[1][j] = j

for i in range(2,n+1):
	for j in range(2,k+1):
		dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[n][k]%1000000000)