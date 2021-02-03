from sys import stdin

n = int(stdin.readline())

wh = [list(map(int,stdin.readline().split())) for _ in range(n)]

ranking = [0 for _ in range(n)]

for i in range(n):
	rank = 1
	for j in range(n):
		if (wh[i][0] < wh[j][0]) and (wh[i][1] < wh[j][1]) and (i!=j):
			rank+=1
	ranking[i] = str(rank)

print(" ".join(ranking))