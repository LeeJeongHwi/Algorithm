from sys import stdin
n = int(stdin.readline())

xy = []

for i in range(n):
	xy.append(tuple(map(int,stdin.readline().split())))

xy.sort(key=lambda x:x[0])
xy.sort(key=lambda x:x[1])

for i in xy:
	print(i[0],i[1])
