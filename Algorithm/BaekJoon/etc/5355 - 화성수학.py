from sys import stdin

n = int(input())

# @ = x3 , % = +5 , # = -7

for i in range(n):
	num = list(stdin.readline().split())
	length = len(num)
	result = float(num[0])
	for j in range(1,length):
		if num[j] == '@':
			result *= 3
		elif num[j] == '%':
			result += 5
		else:
			result -= 7
	print("%.2f"%result)