from sys import stdin
import sys
sys.setrecursionlimit(10**8)

def solve(stack):
	strs = stdin.readline().rstrip()
	if strs=='.':
		return
	if strs=='':
		return solve(stack)

	for s in strs:
		if s=='(' or s=='[':
			stack.append(s)
		if stack and (s==')' or s==']'):
			if s==')':
				if stack.pop()!='(':
					print('no')
					return solve([])
			elif s==']':
				if stack.pop()!='[':
					print('no')
					return solve([])
		elif not stack and (s==')' or s==']'):
			print('no')
			return solve([])
	if strs[-1] != '.':
		return solve(stack)
	else:
		if stack:
			print('no')
			return solve([])
		elif not stack:
			print("yes")
			return solve([])
solve([])