n = int(input())
dp = [0 for _ in range(31)]

dp[2] = 3
dp[0] = 1

#값이 2 증가할 때 마다 2가지의 방법이 더 늘어남 즉 늘어 날 때 마다 *2를 해줘야함

for i in range(4,n+1,2):
	if i % 2 == 0 :
		dp[i] = dp[i-2] * 3 
		for j in range(4,i+1,2):
			if i-j >= 0:
				dp[i] += dp[i-j] * 2

print(dp[n])