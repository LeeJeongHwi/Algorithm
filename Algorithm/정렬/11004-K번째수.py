from sys import stdin

_,k = map(int,stdin.readline().split())

data = list(map(int,stdin.readline().split()))

data.sort()

print(data[k-1])

# 시간이 너무 오래걸림 - 시간초과 날 확률이 큼 하지만 정답?????
# 그렇다 문제가 허점이 많다. 본래의 의도는 Quick Selection을 해야함
