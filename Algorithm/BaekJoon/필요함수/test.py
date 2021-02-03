dp = [0 for _ in range(10001)]
dp[1] = 1
for i in range(2,10001):
	dp[i] = dp[i-2]+dp[i-1]
print(dp[8181])