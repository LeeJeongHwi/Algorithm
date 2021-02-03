# append 와 pop의 시간이 많이 걸리는가?
# Queue vs List

from sys import stdin

n,k = map(int,stdin.readline().split())

arr = [i for i in range(1,n+1)]
result = []

i = k-1
while True:
	result.append(arr.pop(i))
	if not arr:
		break
	i = (i+k-1) % len(arr)

answer = ''
for i in range(0,n):
	answer += str(result[i])+', '
print("<"+answer[:-2]+">")

#pop(0)은 O(N)만큼의 시간이 더 걸린다