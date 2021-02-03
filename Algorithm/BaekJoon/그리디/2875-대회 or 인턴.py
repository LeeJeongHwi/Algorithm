#2명의 여학생, 1명의 남학생

#그리디 방식이라기 보단 완전탐색에 가깝다
from sys import stdin

female , male , intership = map(int,stdin.readline().split())

def createTeam(fe,ma):
	team = 0
	# print("FE,MA : ",fe,ma)
	while (1):
		if fe-2 >= 0:
			fe -= 2
		else:
			break
		if ma-1 >= 0:
			ma -= 1
		else:
			break
		team += 1
	return team


def solution(fe,ma,inter):
	maxTeam = 0
	tfe,tma = 0,0
	for i in range(0,inter+1):
		tfe,tma = fe,ma
		if (tfe-(inter-i)) < 0 or (tma-i) < 0:
			continue
		else:
			reTeam = createTeam(tfe-(inter-i),tma-i)
		if maxTeam < reTeam:
			maxTeam = reTeam
	return maxTeam

print(solution(female,male,intership))


""" 더 깔끔하고 완벽한코드
N,M,K = map(int,input().split())
max = 0
while True:
    N-=2
    M-=1
    if N<0 or M<0 or (N+M)< K:
        break
    max+=1
print(max)
"""