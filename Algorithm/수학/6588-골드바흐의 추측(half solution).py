from sys import stdin
import math
#에라토스테네스의 체
def prime():
	ast = [True] * 1000001
	maxl = math.ceil(math.sqrt(1000000))
	ast[1] = False
	ast[0] = False
	for i in range (2,maxl):
		if ast[i]:
			for j in range(i+i,1000001,i):
				if ast[j] == False:
					continue
				else:
					ast[j] = False
	return ast
#결과값
def calc(arr,n):
	#arr == 소수의 배열	
	arlen = len(arr)//2

	for i in range(arlen+1):
		#solution
		if arr[i]:
			if arr[n-i]:
				return i,n-i

	return "Goldbach's conjecture is wrong."

arr = prime()
	
while True:
	n = int(stdin.readline())
	if n == 0:
		break
	i,j = calc(arr,n)
	print(n,"=",i,"+",j)