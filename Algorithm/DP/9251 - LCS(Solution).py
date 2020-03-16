#solution : https://twinw.tistory.com/126
from sys import stdin

fline = [x for x in stdin.readline().rstrip()]
sline = [x for x in stdin.readline().rstrip()]

f_length = len(fline)
s_length = len(sline)

dp = [[0]*(f_length+1) for _ in range(s_length+1)]

for i in range(s_length):
	for j in range(f_length):
		if fline[j] == sline[i]:
			dp[i][j] = dp[i-1][j-1] + 1
		else:
			dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(max(dp[s_length-1]))