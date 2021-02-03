import itertools
from sys import stdin

n = int(stdin.readline())

matrix = []

for _ in range(n):
	matrix.append(list(map(int,stdin.readline().split())))

def go(p):
	cost = 0
	for i in range(0,n):
		if matrix[p[i]][p[i+1]] !=0 :
			cost += matrix[p[i]][p[i+1]]
		else:
			return -1
	return cost

town =[x for x in range(n)]
minNum = 9876543210
for perArr in itertools.permutations(town):
	perArr+=(perArr[0],)
	result = go(perArr)
	if result == -1:
		continue
	minNum = min(result,minNum)

print(minNum)