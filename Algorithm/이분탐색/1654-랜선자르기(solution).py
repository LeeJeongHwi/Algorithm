"""
solution : https://sungmin-joo.tistory.com/22
"""
from sys import stdin

k,n = map(int,stdin.readline().split())

cable = []
for _ in range(k):
	cable.append(int(stdin.readline()))
cable.sort(reverse=True)

def binary_Search(n,cable):
	high = cable[0]
	low = 0
	result = 0

	while low<=high:
		mid = (high+low) // 2
		# print("NOW mid : ",mid)
		cnt = 0
		if mid == 0 :
			return 1 
		for c in cable:
			cnt += c//mid
			if cnt >= n and mid >= result :
				result = mid
				break
		# print("NOW CNT",cnt)
		if cnt < n :
			high = mid - 1
		else:
			low = mid + 1

	return result
		# print("NOW HIGH LOW ",high,low)
		# print("============================")
print(binary_Search(n,cable))