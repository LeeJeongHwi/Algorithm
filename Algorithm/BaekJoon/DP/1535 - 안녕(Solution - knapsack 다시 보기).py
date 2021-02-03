# 모든 경우를 탐색하는 경우
"""
from sys import stdin
from itertools import combinations
n = int(stdin.readline())
lose_health = list(map(int,stdin.readline().split()))
get_happy = list(map(int,stdin.readline().split()))


max_happy = 0 
for i in range(1,n+1):
	for line in combinations(range(0,n),i):
		health = 100
		happy = 0
		for x in line:
			health -= lose_health[x]
			if health <= 0:
				break
			happy += get_happy[x]
		max_happy= max(max_happy,happy)
print(max_happy)
"""

from sys import stdin
n =int(stdin.readline())
lose_health = [0]+list(map(int,stdin.readline().split()))
get_happy = [0]+list(map(int,stdin.readline().split()))

dp = [[0 for _ in range(101)] for _ in range(n+1)] 
#dp [i][j] = i 번째 사람까지 인사하고 남은 체력이 j일때 최대 기쁨
#dp [0][99] = 1 번째 사람까지 인사하고 남은 체력이 99 일때 최대 기쁨 

for i in range(1,n+1):
	for j in range(1,101):
		if lose_health[i] >= j: #현재 hp보다 잃는 hp보다 많을 때
			dp[i][j] = dp[i-1][j] #한명과 더 인사하기 전, 남은 hp
		else:
			dp[i][j] = max(dp[i-1][j],dp[i-1][j-lose_health[i]]+get_happy[i])
			#dp [i-1][j] == 한명과 인사하기 전(남은hp는 j)일 때 최대 기븜
			#dp[i-1][j-lose_health[i]]+get_happy[i] == 한명과 인사하고, lose_health[i] 만큼 소진하고, get_happy[i]만큼 기쁨을 얻을 때
# for i in dp:
# 	print(i)
#정답
print(dp[n][100])