from sys import stdin

t = int(input())

def solution():
	n = int(stdin.readline())
	part = [tuple(map(int,stdin.readline().split())) for _ in range(n)]
	part.sort(key=lambda x:x[0])
	count = 0
	min_Rank = part[0][1]
	for i in range(1,n):
		if (min_Rank > part[i][1]):
			min_Rank = part[i][1]
		else:
			count+=1
	print(n-count)

for _ in range(t):
	solution()