from sys import stdin

n = int(stdin.readline())

correct = set(map(int,stdin.readline().split()))

# correct.sort()

m = int(stdin.readline())

haveCard = list(map(int,stdin.readline().split()))

# ans = ['0' for _ in range(m)]
# #=============================================
# def solution(n,m,target):
# 	#각각에 대해서 이분 탐색을 진행
# 	end = n-1
# 	start = 0

# 	while start<=end:
# 		mid = (start+end)//2
# 		if target == correct[mid]:
# 			return True
# 		if target >= correct[mid]: #mid의 기준보다 오른쪽에 있다(크다) 
# 			start = mid+1
# 		elif target < correct[mid]: #mid의 기준보다 왼쪽에 있다(작다)
# 			end = mid-1
# 	return False

# for i in range(m):
# 	target = haveCard[i]
# 	if solution(n,m,target):
# 		ans[i] = '1'
# print(' '.join(ans))  ==> 이분탐색으로 했으나 시간이 많이 걸림

for c in haveCard:
	if c in correct:
		print(1,end=' ')
	else:
		print(0,end=' ')

