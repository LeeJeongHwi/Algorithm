from sys import stdin
from itertools import combinations
stdin = open("input.txt","r")

n = int(stdin.readline())
"""
3장의 카드를 골라 합을 구한 후 일의 자리 수가 가장 큰 사람이 게임을 이김
"""
max_score = 0
max_score_person = 0
for i in range(n):
    numlist = list(map(int,stdin.readline().split()))
    for l in combinations(numlist,3):
        sums = sum(l)%10
        if max_score < sums:
            max_score = sums
            max_score_person = i
        elif max_score == sums and max_score_person < i:
            max_score_person = i
print(max_score_person+1)