#자기점수 중 최댓값 = M
#새로운 점수 = 점수/M * 100
#새로운 점수들의 평균 (0.2f로 표현)
from sys import stdin
input()
nList = list(map(int,stdin.readline().split()))
newNum = []
m = max(nList)

for i in nList:
	newNum.append((i/m)*100)
print(format(sum(newNum)/len(newNum),'0.2f'))

#다른 사람 풀이

# input()
# *i, = map(int,input().split())
# print(sum(i)/max(i)/len(i)*100)