from sys import stdin
n = int(input())
for i in range(n):
	print(sum(map(int,stdin.readline().split())))