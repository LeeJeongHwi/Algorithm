from sys import stdin

_ , m = map(int,stdin.readline().split())

height = [int(x) for x in stdin.readline().split()]
height.sort(reverse=True)

def binary_Search(m,arr):
	result = 0
	start = 0
	end = arr[0]
	while (start<=end) :
		mid = (start+end) // 2
		cnt = 0
		for w in arr:
			if w-mid >= 0:
				cnt += w-mid
			if cnt >= m and result < mid:
				result = mid
		if cnt > m :
			start = mid + 1
		else:
			end = mid - 1
	return result

print(binary_Search(m,height))

"""
PyPy3 으로 성공 // Python3 으로는 시간 초과
"""