arr=[4,4,4,3,3]

def solution(arr):
    l = len(arr)
    ans = []
    if l == 0:
        return []
    else:
        ans.append(arr[0])
    for i in range(1,l):
        if arr[i] != arr[i-1]:
            ans.append(arr[i])
        else:
            continue
    return ans
print(solution(arr))