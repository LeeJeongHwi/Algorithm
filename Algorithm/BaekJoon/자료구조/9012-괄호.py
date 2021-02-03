from sys import stdin

def exec(st,arr):
	stlen = len(st)
	for i in range(stlen):
		if st[i] == '(':
			arr.append(st[i])
		elif st[i] == ')':
			if not arr:
				return "NO"
			else:
				arr.pop()
	if arr:
		return "NO"
	else:
		return "YES"

n = int(stdin.readline())

for i in range(n):
	st = stdin.readline().rstrip()
	arr = []
	print(exec(st,arr))