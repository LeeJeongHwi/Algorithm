n = int(input())

dp = [[0 for col in range(2)] for row in range(91)]

dp[1][1] = 1

for i in range(2,n+1):
	for j in range(2):
		if j == 0 :
			dp[i][j] = dp[i-1][j+1] + dp[i-1][j]
		else:
			dp[i][j] = dp[i-1][j-1]

sum = 0 
for i in range(2):
	sum += dp[n][i]
print(sum)