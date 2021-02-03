from sys import stdin
n = int(stdin.readline())
alcho = [0 for _ in range(n+1)]
dp = [0 for _ in range(n+1)]
for i in range(1,n+1): #입력값
	alcho[i] = int(stdin.readline())

dp[0] = alcho[0]

for i in range(1,n+1):
	if i<3:
		dp[i]=alcho[i]+alcho[i-1]
	else:
		dp[i]=max((dp[i-1]),(alcho[i]+alcho[i-1]+dp[i-3]),(alcho[i]+dp[i-2]))
print(dp[n])