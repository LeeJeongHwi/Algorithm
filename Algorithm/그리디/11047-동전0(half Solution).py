from sys import stdin

#init
n , goal = map(int,stdin.readline().split())
cnt = 0
coin = []
for _ in range(n):
	n = int(stdin.readline())
	if n <= goal:
		coin.append(n)
coinlen = len(coin)

def greedy(goal,cl):
	global cnt
	i = 0
	while goal!=0:
		selectCoin = coin[cl-i]
		if goal >= selectCoin:
			cnt += (goal//selectCoin)
			goal = goal%selectCoin
		else:
			i+=1
greedy(goal,coinlen-1)
print(cnt)