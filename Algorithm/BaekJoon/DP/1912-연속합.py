from sys import stdin

n = int(input())
A = list(map(int,stdin.readline().split()))
dp = [0 for _ in range(n)] #최대값 넣기

dp[0] = A[0]

for i in range(1,n):
	dp[i] = max(dp[i-1]+A[i],A[i])
print(max(dp))