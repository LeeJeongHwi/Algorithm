arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

def solution(arr1,arr2):
    ans = []
    for a,b in (zip(arr1,arr2)):
        subAns = []
        for c,d in (zip(a,b)):
            subAns.append(c+d)
        ans.append(subAns)
    return ans
print(solution(arr1,arr2))