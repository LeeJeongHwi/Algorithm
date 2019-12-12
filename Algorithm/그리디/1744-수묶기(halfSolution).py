"""
half Solution : https://m.blog.naver.com/pjok1122/221652191176
"""
from sys import stdin

n = int(stdin.readline())
numArr_pos = []
numArr_neg = []
ans = 0
for _ in range(n):
	num = int(stdin.readline())
	if num == 1:
		ans += num
	elif num <= 0:
		numArr_neg.append(num) #neg의 가장 큰 수는 0
	else:
		numArr_pos.append(num) #pos의 가장 작은 수는 1
numArr_pos.sort(reverse=True)
numArr_neg.sort()

def solution(n):
	global ans
	poslen = len(numArr_pos)
	neglen = len(numArr_neg)

	for i in range(0,poslen,2):
		if (i+1) < poslen:
			ans+=numArr_pos[i]*numArr_pos[i+1]
		else:
			ans+=numArr_pos[i]
	for i in range(0,neglen,2):
		if (i+1) < neglen:
			ans+=numArr_neg[i]*numArr_neg[i+1]
		else:
			ans+=numArr_neg[i]
if n != 0:
	solution(n)
	print(ans)
else:
	print(ans)