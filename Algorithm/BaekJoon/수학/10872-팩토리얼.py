from sys import stdin

n = int(stdin.readline())
re=1
if n == 0:
	print(re)
else:
	for i in range(1,n+1):
		re*=i
	print(re)