from sys import stdin

t = int(stdin.readline())

fList = {}
for _ in range(t):
	friends = int(stdin.readline())
	for _ in range(friends):
		a,b = stdin.readline().split()
		if fList not in a:
			