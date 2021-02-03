from sys import stdin

n = int(stdin.readline())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]
#0->1 1->2 2->1

for k in range(n):
	for i in range(n):
		for j in range(n):
			if maps[i][j] == 1:
				maps[i][j] = 1
			else:
				if maps[i][k] == 1:
					if maps[k][j] == 1:
						maps[i][j] = 1
for l in maps:
	print(' '.join(map(str,l)))