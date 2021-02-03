from sys import stdin
from collections import Counter
n = int(input())

a = []
b = []
c = []
d = []

for _ in range(n):
	num = list(map(int,stdin.readline().split()))
	a.append(num[0])
	b.append(num[1])
	c.append(num[2])
	d.append(num[3])

cd = []

for i in range(n):
	for j in range(n):
		cd.append(c[i]+d[j])

cnt = 0
cddict = Counter(cd)

for i in range(n):
	for j in range(n):
		s = a[i] + b[j]
		if -s in cddict:
			cnt += cddict[-s]

print(cnt)