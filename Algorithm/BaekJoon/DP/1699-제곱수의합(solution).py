n = int(input())

dp = [i for i in range(n+1)]

for i in range(2,n+1):
	j=1
	while (j**2)<=i:
		dp[i] = min(dp[i],dp[i-(j**2)]+1)
		j+=1

print(dp[n])
