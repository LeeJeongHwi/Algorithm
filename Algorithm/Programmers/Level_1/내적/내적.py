a = [1,2,3,4]
b = [-3,-1,0,2]

def solution(a,b):
    result = 0
    for i in range(len(a)):
        result += a[i]*b[i]
    return result
print(solution(a,b))