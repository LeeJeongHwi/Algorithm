n = int(input())

dp = [[0 for col in range(10)] for row in range(1001)]
#col은 수 row는 자릿수
for i in range(10):
	dp[1][i] = 1

for i in range(2,n+1):
	for j in range(10):
		if j==0:
			dp[i][j] = dp[i-1][j]
		else:
			dp[i][j] = dp[i][j-1]+dp[i-1][j]


sum =0
for i in range(10):
	sum += dp[n][i]

print(sum%10007)
