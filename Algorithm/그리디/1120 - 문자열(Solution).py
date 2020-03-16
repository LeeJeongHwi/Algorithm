#Solution : https://m.blog.naver.com/pjok1122/221652178029
from sys import stdin

A,B = stdin.readline().rstrip().split()

index = len(B) - len(A) + 1

ans = 50

for i in range(index):
	count = 0
	for j in range(len(A)):
		if A[j] != B[i+j]:
			count+=1
	ans = min(ans,count)
print(ans)