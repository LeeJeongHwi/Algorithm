#다른 사람 풀이 --------
from sys import stdin
S = stdin.readline().rstrip()
cg = ["c=","c-","dz=","d-","lj","nj","s=","z="]
for st in cg:
	S = S.replace(st,'*')
print(len(S))


