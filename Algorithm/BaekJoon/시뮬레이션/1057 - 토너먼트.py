from sys import stdin
n,kims,lims = map(int,stdin.readline().split())
#김지민의 번호는 항상 작음
part =[False for x in range(1,n+1)]
part[kims-1] = True
part[lims-1] = True

def tment(npart,roundNum,pn):
	newpart =[]
	if pn%2 == 0:
		for i in range(0,pn,2):
			if npart[i] and npart[i+1]:
				return roundNum
			else:
				if npart[i]:
					newpart.append(npart[i])
				elif npart[i+1]:
					newpart.append(npart[i+1])
				else:
					newpart.append(npart[i])
		return tment(newpart,roundNum+1,len(newpart))
	elif pn%2 == 1:
		for i in range(0,pn-1,2):
			if npart[i] and npart[i+1]:
				return roundNum
			else:
				if npart[i]:
					newpart.append(npart[i])
				elif npart[i+1]:
					newpart.append(npart[i+1])
				else:
					newpart.append(npart[i])
		newpart.append(npart.pop())
		return tment(newpart,roundNum+1,len(newpart))
print(tment(part,1,n))
#효율적인 코드

round = 0
kims-=1
lims-=1
while kims != lims: #같은 경기 일 때
	kims//=2
	lims//=2
	round+=1
	#//=2 를 하면 해당하는 경기 번호가 됨
print(round)