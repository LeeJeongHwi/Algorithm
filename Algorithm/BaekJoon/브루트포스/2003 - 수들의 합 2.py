from sys import stdin

n, m = map(int,stdin.readline().split())

arr = list(map(int,stdin.readline().split()))

right,left = 0,0
result = 0
cnt = 0
while (1):	
	if result >= m:
		result -= arr[left]
		left += 1
	elif right == n:
		break
	else:
		result += arr[right]
		right += 1
	if result == m :
		cnt +=1

print(cnt)
