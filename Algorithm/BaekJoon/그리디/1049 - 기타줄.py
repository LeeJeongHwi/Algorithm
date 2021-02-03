from sys import stdin

broken , brand = map(int,stdin.readline().split())
#6개 패키지 가격 / 낱개로 살 때의 가격

price = []

for i in range(brand):
	price.append(list(map(int,stdin.readline().split())))

price_set = sorted(price,key=lambda x:x[0])
price_sin = sorted(price,key=lambda x:x[1])

def solve():
	if broken < 6:
		return min(price_sin[0][1] * broken,price_set[0][0]*1)
	elif broken % 6 == 0:
		return min(price_set[0][0] * (broken//6),(price_sin[0][1] * broken))
	else:
		#1. 셋트 + 낱개
		set_and_sin = (broken//6)*price_set[0][0] + (broken%6)*price_sin[0][1]
		#2. 셋트(초과하게)
		set_Excess = ((broken//6)+1) * price_set[0][0]
		#3. 낱개 전부
		sin_all = broken * price_sin[0][1]
		return min(set_and_sin,set_Excess,sin_all)

print(solve())
