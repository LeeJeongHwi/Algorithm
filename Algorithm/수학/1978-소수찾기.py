#에라토스테네스의 체
import math
import time
from sys import stdin
n = int(stdin.readline())
arr = [x for x in list(map(int,stdin.readline().split()))]

pri = [True if i != 1 else False for i in range(1001) ]

max_length = math.ceil(math.sqrt(1000))

for i in range(2,max_length):
	if n == 0:
		break
	#True 일 경우 소수
	if pri[i]:
		for j in range(i+i,1001,i):
			if pri[j] == False:
				continue
			pri[j] = False

count = 0
for i in arr:
	if pri[i] == True:
		count+=1 
print(count)