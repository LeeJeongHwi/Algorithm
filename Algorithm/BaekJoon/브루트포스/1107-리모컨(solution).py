"""
Solution : https://br-brg.tistory.com/19
"""
from sys import stdin

channel = int(stdin.readline()) #가고싶은 채널
m = int(stdin.readline()) #안되는 버튼의 개수

if m > 0:
	malf = stdin.readline().rstrip().split() #안되는 버튼
else:
	malf= []

ch = []
curr = 100

for c in range(0, 1000000+1):
	isCont = True
	for str_c in str(c):
		if str_c in malf: #숫자가(c) 안되는 버튼에 있다면?
			isCont = False
			break
	if isCont:
		ch.append(c)

min_diff = 987654321 #??

val = ''

for i in ch: 
	if abs(i-channel) < min_diff: #뽑아낸 값 중에서 가고싶은 채널을 뺏을 때(절대값) 작은 것
		min_diff = abs(i-channel)
		val = str(i)
answer = len(val)+abs(min_diff) #이해못함
answer = min(abs(channel-curr),answer)

print(answer)