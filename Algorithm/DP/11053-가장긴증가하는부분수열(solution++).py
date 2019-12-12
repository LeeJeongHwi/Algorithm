from sys import stdin
n = int(stdin.readline())
A = list(map(int,stdin.readline().split()))
dp = [0 for _ in range(n)]

for i in range(0,n):
	for j in range(0,i):
		if A[i] > A[j] and dp[i] < dp[j] :
			dp[i] = dp[j]
	dp[i]+=1
print(max(dp))