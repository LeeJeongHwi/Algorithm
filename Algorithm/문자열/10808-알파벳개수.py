from sys import stdin

st = stdin.readline().rstrip()
arr = [0 for _ in range(26)]
dc = {}

for i in st:
	if i not in dc:
		dc[i] = 1
	else:
		dc[i] += 1

for i in range(97,123):
	if chr(i) in dc:
		arr[i-97] += dc[chr(i)]

for i in arr:
	print(i,end=' ')