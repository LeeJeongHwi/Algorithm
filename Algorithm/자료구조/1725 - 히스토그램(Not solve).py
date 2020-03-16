from sys import stdin

st = []

n = int(stdin.readline())

ans = 0

for i in range(n+1):
	data = int(stdin.readline())
	if (not st) or (st[-1] < data) :
		st.append(data)
		continue
	while (st and st[-1] >= data):
		h = st.pop()
		