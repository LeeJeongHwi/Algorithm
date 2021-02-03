from sys import stdin
n = int(stdin.readline())
card = stdin.realine().split().rstrip()
m,k = map(int,stdin.readline().split())
dp = [0 for _ in range(n+1)]

