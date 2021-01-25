arr=[5,9,7,10]
divisor = 5

def solution(arr,divisor):
    ans = []
    for i in arr:
        if i%divisor==0:
            ans.append(i)
    if ans:
        return sorted(ans)
    else:
        return -1

print(solution(arr,divisor))