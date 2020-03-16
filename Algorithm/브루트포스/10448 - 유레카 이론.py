from sys import stdin

n = int(input())

num = []
for i in range(1,45):
	num.append((i*(i+1))/2)

def eureka(target):
	for i in num:
		for j in num:
			for k in num:
				if i+j+k == target:
					return 1
	return 0


for i in range(n):
	t = int(stdin.readline())
	print(eureka(t))