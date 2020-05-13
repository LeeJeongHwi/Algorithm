#solution : https://pacific-ocean.tistory.com/200
from sys import stdin

n , k =map(int,stdin.readline().split())
dp = [0]*(k+1)
dp[0] = 1
coin = [int(stdin.readline()) for _ in range(n)]

for i in coin:
	for j in range(i,k+1):
		dp[j] += dp[j-i]

print(dp[k])
