from sys import stdin
n = int(stdin.readline())

xy = []

for i in range(n):
	xy.append(tuple(map(int,stdin.readline().split())))

sxy = sorted(xy)

for i in sxy:
	print(i[0],i[1])
