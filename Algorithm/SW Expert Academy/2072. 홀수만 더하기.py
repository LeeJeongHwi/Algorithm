from sys import stdin

n = int(stdin.readline())
for i in range(n):
	print("#"+str(i+1),sum([x for x in list(map(int,stdin.readline().split())) if x%2==1]))
