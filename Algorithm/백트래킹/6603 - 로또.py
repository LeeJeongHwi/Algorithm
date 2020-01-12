from itertools import combinations
from sys import stdin
while True:
	n = stdin.readline().rstrip().split()
	if not int(n[0]):
		break

	numList = n[1:]

	for i in combinations(numList,6):
		print(' '.join(i))

	print()
""" https://www.acmicpc.net/source/16777311 - BackTracking 으로 푼 것 
from sys import stdin

visit = [False]*50

def backtracking(idx,cnt,lists):
	if cnt == 6:
		tmp = []
		for i in range(len(lists)):
			if visit[i]:
				tmp.append(lists[i]) 
		print(' '.join(map(str,tmp)))
		return
	for i in range(idx,len(lists)):
		if visit[i]:
			continue
		visit[i] = True
		backtracking(i,cnt+1,lists)
		visit[i] = False

while True:
	n = list(map(int,stdin.readline().split()))
	if not n[0]:
		break
	lists = n[1:]
	backtracking(0,0,lists)
	print()
"""