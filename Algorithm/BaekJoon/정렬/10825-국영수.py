from sys import stdin

n = int(stdin.readline())
stu = []

# value == 이름 국어 영어 수학

for i in range(n):
	stu.append(tuple(stdin.readline().split()))

stu.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))



for x in stu:
	print(x[0])