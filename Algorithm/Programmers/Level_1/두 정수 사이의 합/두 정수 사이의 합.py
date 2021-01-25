a = 5
b = 3

def solution(a,b):
    if a<b : return sum([x for x in range(a,b+1)])
    else: return sum([x for x in range(b,a+1)])

print(solution(a,b))