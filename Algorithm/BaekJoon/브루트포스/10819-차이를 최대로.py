from sys import stdin
import itertools

n = int(stdin.readline())

arr = list(map(int,stdin.readline().split()))

maxNum = 0

def solution():
	global maxNum
	
	for perArr in itertools.permutations(arr):
		result = 0
		for i in range(2,n+1):
			result += abs(perArr[i-2]-perArr[i-1])
		if maxNum < result:
			maxNum = result

solution()
print(maxNum)