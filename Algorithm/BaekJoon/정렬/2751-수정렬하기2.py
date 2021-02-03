from sys import stdin

n = int(stdin.readline())

arr = []

for i in range(n):
	arr.append(int(stdin.readline()))

upArr = sorted(arr)

for i in upArr:
	print(i)
#비효율적인 솔트 == 이게 가장 최적의 솔트