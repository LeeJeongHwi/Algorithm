from sys import stdin

lst = list(stdin.readline().rstrip())
rst = []
n = int(stdin.readline())

for i in range(n):
	x = stdin.readline().split()
	if x[0]=='P':
		lst.append(x[1])
	elif x[0]=='L':
		if lst:
			rst.append(lst.pop())
	elif x[0]=='D':
		if rst:
			lst.append(rst.pop())
	else:
		if lst:
			lst.pop()

for i in lst:
	print(i,end='')
for j in range(len(rst)-1,-1,-1):
	print(rst[j],end='')
"""
from sys import stdin

st = list(stdin.readline().rstrip())
n = int(stdin.readline())
lst = len(st)
dex = lst

for i in range(n):
	x = stdin.readline().split()
	if x[0]=='P':
		st.insert(dex,x[1])
		dex += 1
	elif x[0]=='L':
		if dex > 0:
			dex -= 1
	elif x[0]=='D':
		if dex < len(st):
			dex += 1
	else:
		if dex > 0:
			st.pop(dex-1)
			dex-=1
for i in st:
	print(i,end='')
"""
# ==> 시간초과