from sys import stdin

n = int(stdin.readline())

rope = [int(stdin.readline()) for _ in range(n)]

rope.sort(reverse=True)

ans = 0

for i in range(n):
	ans = max(ans,rope[i]*(i+1))
print(ans)