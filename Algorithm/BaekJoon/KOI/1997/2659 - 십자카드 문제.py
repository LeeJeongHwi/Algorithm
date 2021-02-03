#시계수 계산
def calcNumber(nlist):
	clockNumber = 9999
	for i in range(4):
		number=nlist[i%4]*1000+nlist[(i+1)%4]*100+nlist[(i+2)%4]*10+nlist[(i+3)%4]
		clockNumber = min(clockNumber,number)
	return clockNumber

nlist = list(map(int,input().split()))
targetNumber = calcNumber(nlist)

visit = [0 for _ in range(9999)]
def solve():
	count = 0
	for i in range(1,10):
		for j in range(1,10):
			for k in range(1,10):
				for l in range(1,10):
					num = calcNumber([i,j,k,l])
					if num < targetNumber and not visit[num]:
						visit[num]=1
						count+=1
	return count
print(solve()+1)