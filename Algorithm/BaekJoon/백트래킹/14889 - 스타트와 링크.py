#Half solution: https://www.acmicpc.net/board/view/43781
from sys import stdin
n = int(input())
team = [False for _ in range(n)]
startlink = [list(map(int,stdin.readline().split())) for _ in range(n)]
minv=101
def calcStatus(teams):
	global minv
	start,st_Status=[],0
	link,li_Status=[],0
	for i in range(n):
		if teams[i]:
			start.append(i)
		else:
			link.append(i)
	for i in range(n//2):
		for j in range(i+1,n//2):
			st_Status += startlink[start[i]][start[j]]+startlink[start[j]][start[i]]
			li_Status += startlink[link[i]][link[j]]+startlink[link[j]][link[i]]
	minv= min(abs(st_Status-li_Status),minv)


def dvide_Team(cnt,idx):
	if cnt == n//2:
		calcStatus(team)
		return

	for i in range(idx,n):
		if team[i]:
			continue
		team[i]=True
		dvide_Team(cnt+1,i)
		team[i]=False

dvide_Team(0,1)
#0,0 이 아니라 0,1을 넣는 이유는 0을 항상 link팀에 넣겠다는 뜻
#중복을 제거 <<
print(minv)
#####
#Solution : https://hwiyong.tistory.com/307
#Combinations를 이용한 방법
#####
# from itertools import combinations
# from sys import stdin

# n = int(input())
# board = [list(map(int,stdin.readline().split())) for _ in range(n)]

# numlist = [i for i in range(n)]
# res= float('inf')

# def solution():
# 	global res

# 	for cand in combinations(numlist,n//2):
# 		start = combinations(list(cand),2)
# 		link = combinations(list(set(numlist)-set(cand)),2)

# 		s_s = 0
# 		l_s = 0

# 		for x,y in start:
# 			s_s += board[x][y] + board[y][x]
# 		for x,y in link:
# 			l_s += board[x][y] + board[y][x]

# 		res = min(res,abs(s_s-l_s))
# solution()
# print(res)

