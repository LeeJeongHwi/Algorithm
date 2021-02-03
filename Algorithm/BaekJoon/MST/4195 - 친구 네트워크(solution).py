#solution : https://chancoding.tistory.com/50
from sys import stdin

def find(x):
	if parent[x] == x:
		return x
	parent[x] = find(parent[x])
	return parent[x]

def union(x,y):
	x,y = find(x),find(y)
	if x != y:
		parent[y] = x
		number[x] += number[y]
	print(number[x])
t = int(input())
for _ in range(t):
	n = int(stdin.readline())
	parent = {}
	number = {}
	for _ in range(n):
		a,b = stdin.readline().rstrip().split()
		if a not in parent:
			parent[a] = a
			number[a] = 1
		if b not in parent:
			parent[b] = b
			number[b] = 1
		union(a,b)
