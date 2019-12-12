from sys import stdin

n = int(stdin.readline())
arr = []
for i in range(n):
	arr.append(tuple(stdin.readline().split()))

arr = list(enumerate(arr))
arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:int(x[1][0]))

for i in range(n):
	print(arr[i][1][0],arr[i][1][1]