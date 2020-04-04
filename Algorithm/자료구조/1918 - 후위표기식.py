from sys import stdin

exp = list(stdin.readline().rstrip())

def solve():
	stack = []
	ans= ''
	for e in exp:
		if e in '+-*/()':
			if not stack:
				stack.append(e)
				continue
			if e in '+-':
				while stack and stack[-1] not in '(':
					ans+=stack.pop()
				stack.append(e)
			elif e in '*/':
				while stack and stack[-1] not in "+-(":
					ans+=stack.pop()
				stack.append(e)
			elif e == '(':
				stack.append(e)
			elif e == ')':
				while stack and stack[-1]!='(':
					ans+=stack.pop()
				stack.pop()
		else:
			ans+=e
	while stack:
		ans+=stack.pop()
	return ans
print(solve())

# 더 좋은 코드

s = input()
stack = []
pr = {"(":0, ")":0, "+":1, "-":1, "*":2, "/":2}
out = []
for c in s:
    if c in "+-*/":
        while stack and pr[c] <= pr[stack[-1]]: out.append(stack.pop())
        stack.append(c)
    elif c == "(": stack.append(c)
    elif c == ")":
        while stack and stack[-1] != "(": out.append(stack.pop())
        stack.pop()
    else: out.append(c)
while stack: out.append(stack.pop())

print(''.join(out))