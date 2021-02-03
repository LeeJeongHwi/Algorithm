from sys import stdin

def prefixSum(prSum):
   for i in range(1,n+1):
      prSum[i] = prSum[i-1]+nlist[i]

n,m = map(int,stdin.readline().split())
prSum = [0 for _ in range(n+1)]
nlist = [0]+list(map(int,stdin.readline().split()))
prSum[1] = nlist[0]
prefixSum(prSum)
for _ in range(m):
   a,b = map(int,stdin.readline().split())
   print(prSum[b]-prSum[a-1])