#이해가 안되는 문제... 수학...^^..
# python으로 완탐으로 풀면 시간초과가 일어남
from sys import stdin
stdin = open("input.txt","r")

n = int(stdin.readline())
count = 0
for a in range(1,n):
    if n<=3*a and 2*a < n:
        # print(a,(n-a-1)//2)
        count += a-(n-a-1)//2
print(count)