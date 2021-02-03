"""
solution : https://www.acmicpc.net/source/9174216
"""
from sys import stdin

n = int(stdin.readline())

arr = [int(x) for x in stdin.readline().split()]

ans = 0 
def mergesort_conquer(arr,left,mid,right):
	global ans
	l = left
	r = mid+1

	result = []

	while l <= mid and r <= right:
		if arr[l] <= arr[r]: #크기가 왼쪽이 더 작을 때
			result.append(arr[l])
			l += 1
		else:
			result.append(arr[r])
			r += 1
			ans += mid - l + 1

	if l > mid: #left 배열에 원소가 남아 있다면?
		for k in range(r,right+1):
			result.append(arr[k])
	else:
		for k in range(l,mid + 1):
			result.append(arr[k])

	arr[left:right+1] = result[0:right-left+1] #바꾼 배열을 arr에 저장 이해 x  
	del result #result 삭제

def mergesort_divide(arr,left,right):
	if left < right:
		mid = (left+right) // 2
		mergesort_divide(arr,left,mid) #left 분할
		mergesort_divide(arr,mid+1,right) #right 분할
		mergesort_conquer(arr,left,mid,right)

mergesort_divide(arr,0,n-1)
print(ans)