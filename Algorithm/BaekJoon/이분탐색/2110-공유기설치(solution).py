"""
Solution : https://blog.naver.com/pjok1122/221652210187
"""
from sys import stdin

n,c = map(int,stdin.readline().split())

router = []

for _ in range(n):
	router.append(int(stdin.readline()))
router.sort()

def routerCount(mid):
	count = 1
	start = router[0]
	for r in router :
		if r != router[0]:
			if mid <= r - start:
				count +=1
				start = r
	return count

def binary_Search(c,router):
	start = 1	
	end = router[-1]-router[0] #가장 큰 값
	result = 0

	while start <= end :
		mid = (start+end)//2
		cnt = routerCount(mid)

		if cnt >= c: #공유기의 갯수가 목표치 이상이라면 정답
			result = mid
			start = mid + 1
		elif cnt < c: #공유기의 갯수가 모자라면 간격을 좁힌다.
			end = mid - 1
	return result
print(binary_Search(c,router))

