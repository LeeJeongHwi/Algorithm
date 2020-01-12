"""
solution : https://rebas.kr/760
시간초과
"""
from sys import stdin

r,c = map(int,stdin.readline().split())

matrix = []

for _ in range(r):
	line = [x for x in stdin.readline().rstrip()]
	matrix.append(line)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

maxNum = 0

alpha = [False] * 26

def backtracking(x,y,cnt):
	global maxNum
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if (0 <= nx < r ) and (0 <= ny < c):
			if not alpha[ord(matrix[nx][ny]) - ord('A')]:
				alpha[ord(matrix[nx][ny]) - ord('A')] = True
				backtracking(nx,ny,cnt+1)
				alpha[ord(matrix[nx][ny]) - ord('A')] = False
	maxNum = max(maxNum,cnt)

alpha[ord(matrix[0][0]) - ord('A')] = True
backtracking(0,0,1)
print(maxNum)