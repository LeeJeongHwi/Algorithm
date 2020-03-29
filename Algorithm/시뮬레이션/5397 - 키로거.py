from sys import stdin
n = int(stdin.readline())

def keyLog(strs):
	leftSt = []
	rightSt = []
	for i in strs:
		if i=='<':
			if leftSt:
				rightSt.append(leftSt.pop())
		elif i=='>':
			if rightSt:
				leftSt.append(rightSt.pop())
		elif i=='-':
			if leftSt:
				leftSt.pop()
		else:
			leftSt.append(i)
	for i in leftSt:
		print(i,end='')
	for i in reversed(rightSt):
		print(i,end='')
	print()
for i in range(n):
	keyLog(stdin.readline().rstrip())