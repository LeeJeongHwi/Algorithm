
from sys import stdin

def exec(stick,st):
	count = 0
	stlen = len(stick)
	for i in range(stlen):
		if stick[i] == '(':
			st.append(stick[i])
		else:
			if stick[i-1] == ')':
				st.pop()
				count+=1
			else:
				st.pop()
				count += len(st)
	return count
if __name__ == '__main__':
	stick = stdin.readline().rstrip()
	st = []
	print(exec(stick,st))
