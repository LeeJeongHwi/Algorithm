from sys import stdin

n = int(stdin.readline())

haveCard = list(map(int,stdin.readline().split()))
haveCardSet= set(haveCard)
haveCardDict = {}

for h in haveCard:
	if h in haveCardDict :
		haveCardDict[h] += 1
	else:
		haveCardDict[h] = 1

m = int(stdin.readline())

guess = list(map(int,stdin.readline().split()))

ans = [0 for _ in range(m)]

index = 0
for g in guess:
	if g in haveCardSet:
		print(haveCardDict[g],end=' ')
	else:
		print(0,end =' ')