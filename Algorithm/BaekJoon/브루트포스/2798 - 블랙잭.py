from sys import stdin
from itertools import combinations

_,m = map(int,stdin.readline().split())

ans = 0
for line in combinations(list(map(int,stdin.readline().split())),3):
	s = sum(line)
	if s <= m:
		ans = max(ans,s)
print(ans)