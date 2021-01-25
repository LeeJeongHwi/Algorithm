from math import sqrt,pow,floor
n = 120

def solution(n):
    print(floor(sqrt(n)),sqrt(n))
    if(floor(sqrt(n)) < sqrt(n)):
        return -1
    return int(pow((sqrt(n)+1),2))

print(solution(n))