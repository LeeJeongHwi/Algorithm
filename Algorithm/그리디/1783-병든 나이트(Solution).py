"""
Solution : https://jaimemin.tistory.com/598
"""
from sys import stdin
#세로가 x 가로가 y
x,y = map(int,stdin.readline().split())

def solution(x,y):
	if x == 1:
		return 1
	elif x == 2:
		#3번 이하만 가능
		return min(4,(y+1)//2) #3회 이하만 가능하므로
	elif x >= 3 :
		if y < 7 :
			#4회 이상을 움직이기 위해선 가로의 길이가 최소 7칸
			return min(4,y) #4회를 초과하면 1,2,3,4조건을 다 써야하니까
							#그전까지는 그냥 같은조건 여러번 써도 됨
		else:
			return y - 2
print(solution(x,y))
