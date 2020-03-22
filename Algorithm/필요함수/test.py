from itertools import combinations
from sys import stdin

n = int(input())
board = [list(map(int,stdin.readline().split())) for _ in range(n)]

numlist = [i for i in range(n)]
res= float('inf')

def solution():
	global res

	for cand in combinations(numlist,n//2):
		start = combinations(list(cand),2)
		link = combinations(list(set(numlist)-set(cand)),2)

		s_s = 0
		l_s = 0

		for x,y in start:
			s_s += board[x][y] + board[y][x]
		for x,y in link:
			l_s += board[x][y] + board[y][x]

		res = min(res,abs(s_s-l_s))
solution()
print(res)

