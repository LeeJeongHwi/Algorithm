#Solution : https://www.acmicpc.net/board/view/30864
from sys import stdin

n = int(input())

memo = [[0]*3 for _ in range(n)]

matrix = [list(map(int,stdin.readline().split())) for _ in range(n)]

memo[0][0] = matrix[0][0]
memo[0][1] = matrix[0][1]
memo[0][2] = matrix[0][2]

for i in range(1,n):
	for j in range(3):
		if j == 0:
			memo[i][j] = matrix[i][j] + min(memo[i-1][1],memo[i-1][2])
		if j == 1:
			memo[i][j] = matrix[i][j] + min(memo[i-1][0],memo[i-1][2])
		if j == 2:
			memo[i][j] = matrix[i][j] + min(memo[i-1][0],memo[i-1][1])

print(min(memo[n-1]))

