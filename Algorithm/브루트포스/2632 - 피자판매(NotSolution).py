from sys import stdin
from itertools import combinations
#초기값 설정(~line 15)
require_size = int(input())

firstSize , secondSize = map(int,stdin.readline().split())

a = []
b = []

for _ in range(firstSize):
	a.append(int(stdin.readline()))

for _ in range(secondSize):
	b.append(int(stdin.readline()))
#TwoPoint(A,B각각에서만 추출)
cnt = 0
aset = []
bset = []
def twopointer(pizza,pizzaSize,sumset):
	left,right = 0,0
	result = 0
	while True:
		if result >= require_size:
			result -= pizza[left]
			left += 1
		elif right == pizzaSize:
			break
		else:
			result += pizza[right]
			right += 1
			sumset.append(result)
		if result == require_size:
			sumset.append(result)

twopointer(a,firstSize,aset)
twopointer(sorted(a,reverse=True),firstSize,aset)
twopointer(b,secondSize,bset)
twopointer(sorted(b,reverse=True),secondSize,bset)

print(aset)
print(bset)

			
