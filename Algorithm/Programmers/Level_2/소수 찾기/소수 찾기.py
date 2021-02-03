# 에라토스테네스의 체
from itertools import combinations,permutations
from math import ceil,sqrt
n="9999999"
def prime(n):
    primes = [True if i != 1 else False for i in range(n+1)]
    primes[0] = False
    primes[1] = False
    sq = ceil(sqrt(n))
    for i in range(2,sq):
        if primes[i]:
            for j in range(i+i,n+1,i):
                if not primes[j]:
                    continue
                primes[j] = False
    # print(primes)
    return primes

def solution(numbers):
    if n == "0":
        return 0
    count = 0
    nlist = set()
    for i in range(len(numbers)):
        for x in permutations(numbers,i+1):
            nlist.add(int("".join(x)))
    primes = prime(max(nlist))
    for num in nlist:
        if primes[num]:
            # print(num)
            count+=1
    return count
print(solution(n))