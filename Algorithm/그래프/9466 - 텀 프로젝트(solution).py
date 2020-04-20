#solution : https://joosjuliet.github.io/9466/
#싸이클 문제에 대해서 더 해보자..
from sys import stdin

t = int(input())

ans = []
result = 0
def dfs(x,cnt,step):
	#step은 시작 정점
	global student,visit,choice
	#x는 Now
	while True:
		# print("x(now) :",x,"step :",step,"다음 Point :",choice[x])
		# print("visit :",visit)
		# print("Choice :",choice)
		# print("======")
		if visit[x]!=False:
			if step != choice[x]: #시작지점과 다를 때
				return 0
			return cnt-visit[x]
			#탐색된 정점개수 - 사이클 정점에 대한 길이
		visit[x] = cnt #visit는 x에 도착했을 때, 탐색한 개수
		choice[x] = step #start 지점 알려주기
		x = student[x] #다음 정점
		cnt+=1
for _ in range(t):
	n = int(stdin.readline())
	visit = [True]+[False]*(n)
	student = dict()
	choice = [0]+list(map(int,stdin.readline().split()))
	#input
	for i in range(1,n+1):
		student[i] = choice[i]
	# print(student)
	ans = 0
	for i in range(1,n+1):
		if not visit[i]:
			ans+=dfs(i,1,i)
	print(n-ans)


#효율적인 코드:
T=int(input())
for t in range(T):
    n=int(input())
    L=[None]+list(map(int,input().split()))
    visited=[False]*(n+1)
    alone=[]
    for start in range(1,n+1):
        if visited[start]:
            continue
        v=start
        while not visited[v]:
            visited[v]=True
            v=L[v]
        w=start
        while w!=v:
            alone.append(w)
            w=L[w]
    print(len(alone))