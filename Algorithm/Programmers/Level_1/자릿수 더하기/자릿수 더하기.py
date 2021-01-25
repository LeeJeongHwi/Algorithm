n = 987

def solution(n):
    numlist = list(str(n))
    return eval('+'.join(numlist))
print(solution(n))