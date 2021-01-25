n = 12345

def solution(n):
    nlist = reversed([x for x in list(str(n))])
    return [int(x) for x in nlist]

    
print(solution(n))