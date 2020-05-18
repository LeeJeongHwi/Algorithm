from sys import stdin

n,t=map(int,stdin.readline().split())

dp = [0 for _ in range(t+1)]

for _ in range(n):
	k,s = map(int,stdin.readline().split())
	for j in range(t,k-1,-1):
		dp[j] = max(dp[j],dp[j-k]+s)

print(dp[t])

#이거는 왜 안될까?
from sys import stdin

n,t=map(int,stdin.readline().split())

studyTime = [0]
points = [0]
dp = [[0 for _ in range(t+1)] for _ in range(n+1)]

for _ in range(n):
	k,s = map(int,stdin.readline().split())
	studyTime.append(k)
	points.append(s)

for i in range(1,n+1):
	for j in range(studyTime[i],t+1):
		dp[i][j] = max(dp[i-1][j],dp[i-1][j-studyTime[i]]+points[i])

print(dp[n][t])