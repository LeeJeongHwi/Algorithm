#hint : https://www.acmicpc.net/board/view/25052
from sys import stdin

stack = []
strs = stdin.readline().rstrip()
#() = 2
#[] = 3
#(X) = 2*X
#[X] = 3*X
#XY = (XY) = X+Y
def calc(st,s):
	result = 0
	if s==')':
		if st[-1]=='(':
			result+=2
			st.pop()
			st.append(result)
			return True
	elif s==']':
		if st[-1]=='[':
			result+=3
			st.pop()
			st.append(result)
			return True
	while True:
		if not stack:
			return False
		elif st[-1] == '(':
			break
		elif st[-1] == '[':
			break
		result+=st.pop()

	if s == ']':
		if stack:
			if st.pop()!='[':
				return False
		result*=3
	elif s== ')':
		if stack:
			if st.pop()!='(':
				return False
		result*=2
	st.append(result)
	return True
def solve():
	for i in strs:
		# print('s :',i)
		if i in '([':
			stack.append(i)
			# print(stack)
			continue
		if stack:
			if calc(stack,i):
				# print(stack)
				continue
			else:
				# print("안될 때")
				return 0
		else:
			return 0
	for i in stack:
		if i == '(' or i=='[':
			return 0
	return sum(stack)
print(solve())
