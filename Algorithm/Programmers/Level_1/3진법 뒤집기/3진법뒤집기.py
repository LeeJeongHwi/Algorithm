n = 125

def solution(n):
    ans = []
    num = n
    while num!=0:
        ans.append(num%3)
        num //= 3
    l = len(ans)
    answer = 0
    for i in range(l):
        answer+=ans[i]*(3**(l-i-1))
    return answer
print(solution(n))