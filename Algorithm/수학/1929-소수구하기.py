from sys import stdin
n,m = map(int,stdin.readline().split())

ast = [True] * (m+1)

max_length = int(m**0.5)

ast[1] = False
for i in range(2,max_length):
	if ast[i]:
		for j in range(i+i,m+1,i):
			if ast[j] == False:
				continue
			else:
				ast[j] = False

for i in range(n,m+1):
	if ast[i] == True:
		print(i)
