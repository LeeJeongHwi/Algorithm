x = 0
n = 4

def solution(x,n):
    if x == 0:
        return [0]*n
    elif x<0:
        return [-x for x in range(abs(x),(abs(x)*n)+1,abs(x))]
    else:
        return [x for x in range(x,(x*n)+1,x)]
print(solution(x,n))