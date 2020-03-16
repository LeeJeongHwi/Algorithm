from sys import stdin

n = int(stdin.readline())

memo = [[] for _ in range(n)]

memo[0].append(int(stdin.readline()))

for i in range(1,n):
	floor = list(map(int,stdin.readline().split()))
	for j in range(i+1):
		if j == 0:
			memo[i].append(floor[j] + memo[i-1][j])
		elif j == i:
			memo[i].append(floor[j] + memo[i-1][j-1])
		else:
			memo[i].append(max(floor[j]+memo[i-1][j-1],floor[j]+memo[i-1][j]))
print(max(memo[n-1]))


# memo를 만들기보다는 미리 입력받고 안에 요소 값을 바꾸는것이 더 빠름