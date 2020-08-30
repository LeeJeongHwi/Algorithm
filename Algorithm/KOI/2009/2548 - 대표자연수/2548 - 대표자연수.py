from sys import stdin
n = int(stdin.readline())
nlist = list(map(int,stdin.readline().split()))

nlist.sort()
nlistLen = len(nlist)

if nlistLen % 2 == 0:
	print(nlist[(nlistLen//2)-1])
else:
	print(nlist[nlistLen//2])