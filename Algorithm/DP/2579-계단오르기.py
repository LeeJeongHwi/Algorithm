from sys import stdin

n = int(stdin.readline())
A = [0 for _ in range(n+1)]
dp = [0 for _ in range(n+1)]
for i in range(1,n+1):
	A[i] = int(stdin.readline())

dp[1]=A[1]
if n > 1:
	dp[2]=dp[1]+A[2]

for i in range(3,n+1):
	dp [i] = max(A[i]+dp[i-2],A[i]+A[i-1]+dp[i-3])

print(dp[n])