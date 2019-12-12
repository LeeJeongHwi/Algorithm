from sys import stdin

n = int(stdin.readline())

data = {}

for i in range(n):
	x = int(stdin.readline())
	if x in data:
		data[x] += 1
	else:
		data[x] = 1

data = list(data.items())

data.sort(key=lambda x:x[0])
data.sort(key=lambda x:x[1],reverse=True)

print(data[0][0])