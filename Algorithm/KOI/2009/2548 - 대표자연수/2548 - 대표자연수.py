from sys import stdin
stdin = open('input.txt','r')
n = int(stdin.readline())
nlist = list(map(int,stdin.readline().split()))
minNum , minSum = float('inf'),float('inf')
nlist.sort()
print(nlist)
print(minNum,minSum)