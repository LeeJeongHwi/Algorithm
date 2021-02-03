from sys import stdin
T = int(input())

for t in range(T):
	n = int(input())
	dp = [[0 for col in range(n+1)] for row in range(2)]
	sco = [[0 for col in range(n+1)] for row in range(2)]
	for i in range(2):
		dp[i]=list(map(int,stdin.readline().split()))

	sco[0][0] = dp[0][0]
	sco[1][0] = dp[1][0]
	sco[0][1] = dp[1][0] + dp[0][1]
	sco[1][1] = dp[0][0] + dp[1][1]
	
	for i in range(2,n):
		sco[0][i] = max(sco[1][i-1],sco[1][i-2]) + dp[0][i]
		sco[1][i] = max(sco[0][i-1],sco[0][i-2]) + dp[1][i]

	print(max(sco[0][n-1],sco[1][n-1]))
