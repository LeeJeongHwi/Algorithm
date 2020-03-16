from sys import stdin
data = [int(stdin.readline()) for _ in range(9)]

sumd = sum(data)

def solve():
	for i in range(8):
		for j in range(i+1,9):
			if (sumd - data[i] - data[j]) == 100:
				data[i] = 0
				data[j] = 0
				return

solve()
data.sort()
for i in data[2:]:
	print(i)