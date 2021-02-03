from sys import stdin
n = int(stdin.readline())
A = list(map(int,stdin.readline().split()))
dp = [0 for _ in range(n)]
dp2 = dp.copy()
for i in range(0,n):
	for j in range(0,i):
		if A[i] > A[j] and dp[i] < dp[j] : # 증가 순열
			dp[i] = dp[j]
	dp[i] = dp[i]+1

B=list(reversed(A))

for i in range(0,n):
	for j in range(0,i):
		if B[i] > B[j] and dp2[i] < dp2[j] : # 역방향 증가 순열
			dp2[i] = dp2[j]
	dp2[i] = dp2[i]+1

dp2=list(reversed(dp2))

maxNum = 0 
for i in range(n):
	m = dp[i]+dp2[i]-1
	if m > maxNum:
		maxNum = m

print(maxNum)
