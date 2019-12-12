from sys import stdin

_,_ = map(int,stdin.readline().split())

a = list(map(int,stdin.readline().split()))
b = list(map(int,stdin.readline().split()))
print(' '.join(map(str,sorted(a+b))))
