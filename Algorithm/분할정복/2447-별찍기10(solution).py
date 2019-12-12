"""
Solution : https://has3ong.tistory.com/364
"""
from sys import stdin

n = int(stdin.readline())
graph = [[" " for _ in range(n)] for _ in range(n)]

def solution(x,y,n):
	if n == 1:
		graph[x][y] = '*'
		return

	n //= 3
	for i in range(3):
		for j in range(3):
			if i==1 and j==1:
				continue
			else:
				solution(x+i*n,y+j*n,n)


solution(0,0,n)
for i in graph:
	print("".join(i))