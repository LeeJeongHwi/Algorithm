from sys import stdin

def fact(n):
	re=1
	if n == 0:
		return re
	else:
		for i in range(1,n+1):
			re*=i
		return re

#m이 작은수  == r / n이 큰수 == s
n,m = map(int,stdin.readline().split())

r = fact(m)
s = fact(n)
sr = fact(n-m)
print(str(s//r*sr))
re = list(reversed(str(s//r*sr)))
print(re)
count=0
for i in re:
	if i == '0':
		count+=1
	else:
		break
print(count)