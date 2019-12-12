from sys import stdin

n = int(stdin.readline())

arr = [0 for _ in range(10001)]

for i in range(n):
	x = int(stdin.readline())
	arr[x] += 1

for i in range(10001):
	print("{}\n".format(i) * arr[i] , end='')