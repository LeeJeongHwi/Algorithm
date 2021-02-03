from sys import stdin

fut,pre = map(int,stdin.readline().split())
m = int(stdin.readline())
arr = [x for x in list(map(int,stdin.readline().split()))]
arr.reverse()
ten = 0

for i in range(m):
	ten += (fut**i) * arr[i] 

result = []

while ten:
	result.append(ten%pre)
	ten = ten//pre

while result:
	print(result.pop(),end=' ')
#아니쒸 알고리즘은 똑같은데 왜 틀린거냐고