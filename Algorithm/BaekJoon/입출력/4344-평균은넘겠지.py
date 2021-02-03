from sys import stdin
c = int(input())
for i in range(c):
	n,*score = map(int,stdin.readline().split())
	p = [x for x in score if int((sum(score)/n))<x]
	ratio = len(p)/n*100
	print("%0.3f%%"%round(ratio,3))

#다른사람 풀이

# import sys
# for _ in range(int(sys.stdin.readline())):
#     a = list(map(int,sys.stdin.readline().strip().split()))
#     mean = sum(a[1:len(a)])/a[0]
#     print('%.3f'%round(sum(map(lambda x:x>mean, a[1:len(a)]))/a[0]*100,4)+"%")
   