#Solution : https://hwiyong.tistory.com/308
from sys import stdin

n , k = map(int,stdin.readline().split())

# w = 무게 , v = 가치 , 최대가능무게 = k
items = [(0,0)]
# memo = [[0]*(k+1) for _ in range(n+1)]
memo = [0] * (k+1)


for i in range(n):
	items.append(list(map(int,stdin.readline().split())))
### 2차원 memo를 사용시
#i 는 아이템인덱스
#j 는 현재 가질 수 있는 무게
# for i in range(1,n+1):
# 	for j in range(1,k+1):
# 		w,v = items[i][0] , items[i][1]

# 		if j < w:
# 			memo[i][j] = memo[i-1][j]
# 		else:
# 			memo[i][j] = max(memo[i-1][j],v+memo[i-1][j-w])
# print(memo[n][k])

for i in range(1,n+1):
	for j in range(k,1,-1):
		if items[i][0] <= j:
			memo[j] = max(memo[j],memo[j-items[i][0]]+items[i][1])
print(memo[k])