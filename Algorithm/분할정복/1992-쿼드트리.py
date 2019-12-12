"""
전체를 쪼갠다 --> 처음 전체가 0인지 1인지 확인 --> 
①②
③④      --> 1,2,3,4 순으로 탐색
--> 0과 1이 섞여있으니 
순서 -> 왼쪽위 오른쪽위 왼쪽 아래 오른쪽 아래 
"""
from sys import stdin

def insert(graph,n):
	for i in range(n):
		line = [int(x) for x in stdin.readline().rstrip()]
		graph.append(line)

def check(x,y,num):
	for i in range(x,x+num):
		for j in range(y,y+num):
			if graph[x][y] != graph[i][j]:
				return False #다 검사했을 시 모든 숫자가 1혹은 0 일때
	return True

def solution(x,y,num):
	if check(x,y,num):
		print(graph[x][y],end='')
		return

	num //= 2
	print("(",end='')
	for i in range(0,2):
		for j in range(0,2):
			solution(x+i*num,y+j*num,num)
	print(")",end='')
if __name__ == "__main__":
	n = int(stdin.readline())
	graph = []
	ans = []
	insert(graph,n)
	solution(0,0,n)
"""
전체를 쪼갠다 --> 처음 전체가 0인지 1인지 확인 --> 
①②
③④      --> 1,2,3,4 순으로 탐색
--> 0과 1이 섞여있으니 
순서 -> 왼쪽위 오른쪽위 왼쪽 아래 오른쪽 아래 
"""
from sys import stdin

def insert(graph,n):
	for i in range(n):
		line = [int(x) for x in stdin.readline().rstrip()]
		graph.append(line)

def check(x,y,num):
	for i in range(x,x+num):
		for j in range(y,y+num):
			if graph[x][y] != graph[i][j]:
				return False #다 검사했을 시 모든 숫자가 1혹은 0 일때
	return True

def solution(x,y,num):
	if check(x,y,num):
		print(graph[x][y],end='')
		return

	num //= 2
	print("(",end='')
	for i in range(0,2):
		for j in range(0,2):
			solution(x+i*num,y+j*num,num)
	print(")",end='')
if __name__ == "__main__":
	n = int(stdin.readline())
	graph = []
	ans = []
	insert(graph,n)
	solution(0,0,n)
