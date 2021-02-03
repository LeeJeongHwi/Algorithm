"""
Solution : https://sungmin-joo.tistory.com/66
"""
def backtracking(idx):
	for i in range(1,(idx//2) + 1):
		if s[-i:] == s[-2*i:-i]: return -1 #이부분을 이해해야함
	if idx == n:
		for i in range(n):
			print(s[i],end='')
		return 0
	for i in range(1,4):
		s.append(i)
		if backtracking(idx+1) == 0:
			return 0
		s.pop()

n = int(input())
s = []
backtracking(0)