from sys import stdin

n = int(input())
line = [list(map(int,stdin.readline().split())) for _ in range(n)]
line.sort()
dp = [0 for _ in range(n)]

for i in range(n):
	for j in range(0,i):
		if line[i][1] > line[j][1] and dp[i] < dp[j]:
			dp[i] = dp[j]
	dp[i]+=1
print(n-max(dp))