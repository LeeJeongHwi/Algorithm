from sys import stdin

strs = stdin.readline().rstrip()
fire = list(stdin.readline().rstrip())

def solve():
	stack = []
	fireLen = len(fire)
	count = 0
	for s in strs:
		stack.append(s)
		count +=1
		if count >= fireLen:
			if stack[-fireLen:] == fire:
				for i in range(fireLen):
					stack.pop()
					count-=1
	if stack:
		print(''.join(stack))
	else:
		print("FRULA")
solve()