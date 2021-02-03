from sys import stdin

t = int(stdin.readline())

stack = []
for _ in range(t):
	n = int(stdin.readline())
	if n == 0:
		stack.pop()
		continue
	stack.append(n)
print(sum(stack))