from sys import stdin

n = int(stdin.readline())
pi = list(map(int,stdin.readline().split()))
dp = [0 for _ in range(n+1)]

#dp[n]값 넣기 
for i in range(1, n+1):
	for j in range(1,i+1):
		dp[i] = max(dp[i],dp[i-j]+pi[j-1])

print(dp[n])