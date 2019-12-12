#내것은 너무 비효율적으로 풀어서 다른사람 것으로 대체
from sys import stdin

_,X = map(int,stdin.readline().split())

nlist = [x for x in stdin.readline().split() if int(x)<X]
print(' '.join(nlist))
